'''
Tor Circuits Manager

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details.
'''

__version__ = '0.0.1'

from .base import CircuitsManagerBase
from .roundrobin import RoundRobinManager

from .path_builders.custom import CustomPathBuilder
from .path_builders.promiscuous import PromiscuousPathBuilder

from .logger import Logger

class TorCircuitsManager(CircuitsManagerBase, Logger):
    pass
