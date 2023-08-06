'''
Minimalistic asyncio-based Tor Controller

:copyright: Copyright 2023 amateur80lvl
:license: LGPLv3, see LICENSE for details
'''

__version__ = '0.0.4'

from .connection import TorConnection
from .commands import TorCommands, OperationFailed
from .logger import Logger
from . import parsers

class TorController(TorConnection, TorCommands, Logger):
    pass
