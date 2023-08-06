'''
Tor Circuits Manager

The basic implementation of circuits management.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details.
'''

import asyncio
import time
import traceback

from mintc import TorController, OperationFailed, parsers


class CircuitsManagerBase:
    '''
    This class provides the basic circuits management logic.

    The following methods should be provided by path builder:

    * update_fingerprints()
    * create_path()
    * is_path_usable(path)
    * use_path(path)
    * forget_path(path)

    The following properties and methods should be provided by specific circuits manager:

    * max_circuits
    * use_circuit(circ)
    * forget_circuit(circ)
    * choose_circuit()
    * circuits_count() -- the count is maintained by use_circuit/forget_circuit
    '''

    # some defaults
    max_circuits = 10
    fingerprints_update_interval = 3600 * 8

    def __init__(self, controller, concurrency=10, **kwargs):
        self.controller = controller
        self.concurrency = concurrency
        self._fingerprints_last_updated = None
        self._circuits_being_created = dict()
        super().__init__(**kwargs)


    async def __aenter__(self):
        '''
        Enter runtime context.
        '''
        return self


    async def __aexit__(self, exc_type, exc_value, traceback):
        '''
        Exit runtime context.
        '''
        pass


    async def run(self):
        '''
        Run circuits manager.
        '''
        await self.update_fingerprints()
        self._fingerprints_last_updated = time.monotonic()

        try:
            # we need CIRC and STREAM events
            self.controller.set_event_handler(self._handle_event)
            await self.controller.set_events('CIRC', 'STREAM')

            # Collect existing usable circuits.
            # This is especially useful when our controller is restarted.
            await self._collect_existing_cirsuits()

            # grab stream management from Tor
            await self.controller.set_conf('__LeaveStreamsUnattached', '1')

            # Maintain desired number of circuits.
            # Create this many circuits concurrently:
            num_concurrent_circuits = max(3, self.concurrency * self.max_circuits // 100)
            while True:
                await asyncio.sleep(1)

                # check control connection is up
                try:
                    if await self.controller.send_request('GETINFO version') is None:
                        break
                except Exception:
                    self.logger.debug(traceback.format_exc())
                    break

                total_circuits  = self.circuits_count() + len(self._circuits_being_created)
                circuits_needed = self.max_circuits - total_circuits
                if circuits_needed <= 0:
                    # enough circuits for now
                    continue

                num_circuits_to_go = num_concurrent_circuits - len(self._circuits_being_created)
                if num_circuits_to_go <= 0:
                    # too many circuits in progress
                    continue

                for i in range(num_circuits_to_go):
                    # create new path
                    path = self.create_path()
                    if path is None:
                        # not enough relays, re-try later
                        break
                    # start creating circuit
                    self.logger.info('Creating new circuit %s', path)
                    try:
                        circ_id = await self.controller.extend_circuit('0', path)
                    except OperationFailed as e:
                        self.logger.error(e)
                        continue
                    self._circuits_being_created[circ_id] = path

                # update fingerprints
                fingerprints_age = time.monotonic() - self._fingerprints_last_updated
                if fingerprints_age > self.fingerprints_update_interval:
                    self.update_fingerprints()
                    self._fingerprints_last_updated = time.monotonic()

        finally:
            # hand off streams management to Tor
            try:
                await self.controller.set_conf('__LeaveStreamsUnattached', '0')
            except Exception:
                pass

            # turn events off
            try:
                self.controller.set_event_handler(None)
                await self.controller.set_events(None)
            except Exception:
                pass


    async def _collect_existing_cirsuits(self):
        '''
        Get existing circuits and collect reusable ones.
        '''
        async for circ in self.controller.get_circuits():
            if circ['status'] != 'BUILT':
                continue
            if circ['purpose'] != 'GENERAL':
                continue
            if self.is_path_usable(circ['path']):
                self.logger.info('Using existing circuit %s', circ['id'])
                self.use_path(circ['path'])
                self.use_circuit(circ)


    async def _handle_event(self, event):
        '''
        Asynchronous event handler.
        '''
        event_type = parsers.extract_event_type(event)
        if event_type == 'CIRC':
            #self.logger.debug('Event: %s', event)
            circ = parsers.parse_circuit_event(event)
            self._handle_circuit(circ)
            return

        if event_type == 'STREAM':
            #self.logger.debug('Event: %s', event)
            stream = parsers.parse_stream_event(event)
            if stream['status'] == 'NEW':
                await self._handle_new_stream(stream)
            return

        self.logger.error('Unhandled event:\n %s', '\n'.join(event))


    def _handle_circuit(self, circ):
        if circ['status'] == 'BUILT':
            self._circuits_being_created.pop(circ['id'], None)

            if self.is_path_usable(circ['path']):
                self.logger.info('Using created circuit %s', circ['id'])
                self.use_path(circ['path'])
                self.use_circuit(circ)
            else:
                self.logger.info('Rejecting created circuit %s', circ['id'])
                self.forget_path(circ['path'])
                self.forget_circuit(circ)

        elif circ['status'] in ['CLOSED', 'FAILED']:
            self._circuits_being_created.pop(circ['id'], None)

            self.logger.info('%s circuit %s', circ['status'], circ['id'])
            self.forget_path(circ['path'])
            self.forget_circuit(circ)


    async def _handle_new_stream(self, stream):
        '''
        Attach new stream to some circuit.
        '''
        # Don't stuck in here for too long, three attempts only.
        # Tor spec says: Tor will close unattached streams by itself,
        # roughly two minutes after they are born.
        for attempt in range(3):
            circ_id = self.choose_circuit()
            if circ_id is None:
                # oops, no circuits!
                self.logger.error('No circuits to attach stream %s', stream['id'])
                await asyncio.sleep(1)
                continue
            try:
                await self.controller.attach_stream(stream['id'], circ_id)
                self.logger.info('Attached stream %s to circuit %s', stream['id'], circ_id)
                return
            except OperationFailed as e:
                if e.code == '551':
                    # 551 Can't attach stream for some reason. Try again.
                    self.logger.error(e)
                    continue
                elif e.code == '552':
                    # 552 Unknown circuit or stream.
                    self.logger.error(e)
                    if e.message.startswith('Unknown circuit'):
                        # unknown circuit, try again
                        continue
                    else:
                        # unknown stream?
                        break
                elif e.code == '555':
                    # 555 Connection is not managed by controller.
                    self.logger.error(e)
                    break
                else:
                    raise

        if circ_id is not None:
            self.logger.error('Failed attaching stream %s to circuit %s', stream['id'], circ_id)
