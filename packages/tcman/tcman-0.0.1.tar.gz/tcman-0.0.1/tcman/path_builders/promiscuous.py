'''
Tor Circuits Manager

Promiscuous path builder.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details.
'''

from collections import Counter
import random

class PromiscuousPathBuilder:

    def __init__(self, bridge=None, num_hops=3, use_stable=True, use_fast=True, **kwargs):
        self.__bridge = bridge
        self.__use_stable = use_stable
        self.__use_fast = use_fast
        self.__num_hops = num_hops
        self.__fingerprints_in_use = Counter()
        super().__init__(**kwargs)


    async def update_fingerprints(self):
        new_guards = []
        new_middles = []
        new_exits = set()
        async for desc in self.controller.get_network_statuses():
            # filter out relays
            if self.__use_stable and 'Stable' not in desc['flags']:
                continue
            if self.__use_fast and 'Fast' not in desc['flags']:
                continue

            # at first, collect exit nodes
            if 'Exit' in desc['flags']:
                new_exits.add(desc['fingerprint'])
                continue

            if 'Guard' in desc['flags'] and desc['fingerprint'] not in new_exits:
                # On the one hand, we should choose guards carefully.
                # But on the other hand that's makes no sense for short circuits
                # that don't need anonymity.
                new_guards.append(desc['fingerprint'])
            else:
                new_middles.append(desc['fingerprint'])

        self.logger.info('%s guard, %s middle, %s exit relays',
                         len(new_guards), len(new_middles), len(new_exits))
        self._guard_fingerprints = new_guards
        self._middle_fingerprints = new_middles
        self._exit_fingerprints = list(new_exits)


    def create_path(self):
        '''
        Create path for new circuit.
        '''
        fingerprints_in_use = set(self.__fingerprints_in_use)

        # start building path from bridge or guard relay
        if self.__bridge:
            path = [self.__bridge]
        else:
            guards = list(set(self._guard_fingerprints) - fingerprints_in_use)
            if len(guards) == 0:
                self.logger.info('All available %s guard relays are already in use',
                                len(self._guard_fingerprints))
                return None
            path = [random.choice(guards)]

        # add middle relays
        while len(path) < self.__num_hops - 1:
            middles = list(set(self._middle_fingerprints) - fingerprints_in_use - set(path))
            if len(middles) == 0:
                self.logger.info('All available %s middle relays are already in use',
                                 len(self._middle_fingerprints))
                return None
            path.append(random.choice(middles))

        # add exit relay
        exits = list(set(self._exit_fingerprints) - fingerprints_in_use - set(path))
        if len(exits) == 0:
            self.logger.info('All available %s exit relays are already in use',
                             len(self._exit_fingerprints))
            return None
        path.append(random.choice(exits))

        return path


    def is_path_usable(self, path):
        '''
        Path is usable for us if path length matches num_hops.
        '''
        return len(path) == self.__num_hops


    def use_path(self, path):
        '''
        Collect relay fingerprints.
        '''
        for fingerprint in path:
            self.__fingerprints_in_use[fingerprint] += 1


    def forget_path(self, path):
        '''
        Forget relay fingerprints.
        '''
        for fingerprint in path:
            self.__fingerprints_in_use[fingerprint] -= 1
            if self.__fingerprints_in_use[fingerprint] <= 0:
                del self.__fingerprints_in_use[fingerprint]
