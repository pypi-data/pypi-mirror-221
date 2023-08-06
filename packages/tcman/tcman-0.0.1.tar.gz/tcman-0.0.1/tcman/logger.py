'''
Tor Circuits Manager

This module implements the very basic logging
and should be replaced with an asynchronous version
if logging to file is needed.

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details
'''

import logging

class Logger:

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())
