from enum import Enum
import logging

WIDTH = 1920
HEIGHT = 1080

FPS = 60

LOGGER = "Chicken_LOGGER"
_logger:logging.Logger = logging.getLogger(LOGGER)
class LogLevels(Enum):

    INFO = _logger.info
    DEBUG = _logger.debug
    WARNING=_logger.warning
    ERROR = _logger.error


class SettingOptions(Enum):
    Music = "Music"


class Direction(Enum):
    UP = "Up"
    LEFT = "Left"
    DOWN = "Down"
    RIGHT = "Right"


class Objects_Type(Enum):
    RENDER_ABLE = "render"
    MOVE_ABLE = "move"
    DAMAGE_ABLE = "damage"
    DETECT_ABLE = "detect"
    SHOOTERS = "shooter"


PLAYER = "Player"
UPGRADE = "Upgrade"


class Enemy_Typs(Enum):
    def __str__(self):
        return self.value + " Chicken"
    BASE = "Base"
    NORMAL = "Normal"
    CIRCLE = "Circle"


class Egg_Types(Enum):
    def __str__(self):
        return self.value + " Egg"

    Normal = "Normal"


class Shoot_Typs(Enum):
    def __str__(self):
        return self.value + " Shoot"

    NORMAl = "Normal"
    ANGLE = "Angles"
    THREE_ANGLE = "Three Angles"
    FIVE_ANGE = "Five Angles"
