'''
Tor Circuits Manager

Use circuits for streams in round robin way.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details.
'''

class RoundRobinManager:

    def __init__(self, max_circuits=10, **kwargs):
        self.max_circuits = max_circuits
        self.__circuit_ids = []
        self.__circuit_index = 0
        super().__init__(**kwargs)

    def use_circuit(self, circ):
        '''
        Remember circuit path.
        '''
        self.__circuit_ids.append(circ['id'])

    def forget_circuit(self, circ):
        '''
        Forget circuit path.
        '''
        try:
            self.__circuit_ids.remove(circ['id'])
        except ValueError:
            pass

    def choose_circuit(self):
        '''
        Return circuit id.
        '''
        if len(self.__circuit_ids) == 0:
            return None

        if self.__circuit_index >= len(self.__circuit_ids):
            self.__circuit_index = 0

        circ_id = self.__circuit_ids[self.__circuit_index]
        self.__circuit_index += 1

        return circ_id

    def circuits_count(self):
        return len(self.__circuit_ids)
