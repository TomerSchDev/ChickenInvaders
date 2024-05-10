from pygame import constants
from enum import Enum


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


def get_Movement(keys: tuple[bool]):
    UP = (Direction.UP, constants.K_UP, constants.K_w)
    LEFT = (Direction.LEFT, constants.K_LEFT, constants.K_a)
    DOWN = (Direction.DOWN, constants.K_DOWN, constants.K_s)
    RIGHT = (Direction.RIGHT, constants.K_RIGHT, constants.K_d)
    directions = [UP, LEFT, DOWN, RIGHT]
    movement = [False] * 4
    for direction in directions:
        e, a, b = direction
        if keys[a] or keys[b]:
            movement[e.value] = True
    return movement
