'''
Tor Circuits Manager

Custom path builder.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details.
'''

from collections import Counter
import random

class CustomPathBuilder:

    def __init__(self, paths=None, **kwargs):
        self.__paths = paths
        self.__path_index = 0
        super().__init__(**kwargs)

    async def update_fingerprints(self):
        return

    def create_path(self):
        '''
        Choose one of custom path in round robin way.
        '''
        if self.__path_index >= len(self.__paths):
            self.__path_index = 0
        path = self.__paths[self.__path_index]
        self.__path_index += 1
        return path

    def is_path_usable(self, path):
        '''
        Path is usable for us if it matches one in our custom paths.
        '''
        return path in self.__paths

    def use_path(self, path):
        return

    def forget_path(self, path):
        return
