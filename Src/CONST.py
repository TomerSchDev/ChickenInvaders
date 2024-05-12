from enum import Enum

WIDTH = 1920
HEIGHT = 1080

FPS = 60


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class Objects_Type(Enum):
    RENDER_ABLE = "render"
    MOVE_ABLE = "move"
    DAMAGE_ABLE = "damage"
    DETECT_ABLE = "detect"
    SHOOTERS = "shooter"

    def __str__(self):
        return self.value
