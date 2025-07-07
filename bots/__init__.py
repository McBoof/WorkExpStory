"""
Bots Package
Contains all the individual bot implementations for the storytelling program.
"""

# Import all bot classes to make them easily accessible
from .willow_bot import WillowBot
from .kate_bot import KateBot
from .katie_bot import KatieBot
from .sophia_bot import SophiaBot
from .zac_bot import ZacBot
from .zak_bot import ZakBot
from .eden_bot import EdenBot
from .nathan_bot import NathanBot
from .noah_bot import NoahBot
from .samuel_bot import SamuelBot
from .william_bot import WilliamBot

# List of all available bot classes
ALL_BOTS = [
    WillowBot,
    KateBot,
    KatieBot,
    SophiaBot,
    ZacBot,
    ZakBot,
    EdenBot,
    NathanBot,
    NoahBot,
    SamuelBot,
    WilliamBot
]

__all__ = [
    'WillowBot', 'KateBot', 'KatieBot', 'SophiaBot', 'ZacBot', 'ZakBot',
    'EdenBot', 'NathanBot', 'NoahBot', 'SamuelBot', 'WilliamBot', 'ALL_BOTS'
]
