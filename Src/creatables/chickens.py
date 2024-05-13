from typing import Optional

from pygame import Surface, transform
from Src.creatables.egg import abs_Egg, Normal_Egg
from Src.utils import get_image, calculate_points
from Src.interfaces import i_Renderable, i_MoveAble, i_Detectable, i_Shooter
from Src.movment_functions import *
from Src.CONST import *
import random


class ABS_Chicken(i_Renderable, i_MoveAble, i_Detectable, i_Shooter):
    def __init__(self, img: Optional[Surface], pos: tuple[int, int], hp: int, speed, func_m, dir, egg_type, rnd_shot):
        i_Renderable.__init__(self, img, pos)
        i_MoveAble.__init__(self, func_m, speed,pos, img.get_size() if img else (0, 0))
        i_Detectable.__init__(self, pos, self._size, hp, abs_Egg)
        i_Shooter.__init__(self, dir, egg_type, rnd_shot)


class Normal_Chicken(ABS_Chicken):
    def __init__(self, pos: tuple[int, int]):
        img = transform.scale(get_image("chicken"), (100, 100))
        super().__init__(img, pos, 2, 2, in_a_line, Direction.DOWN, Egg_Types.Normal, 30)
        x, y = pos
        self.__speed = 2
        self.__min_x = x - 100
        self.__max_x = x + 100
        directions = [Direction.LEFT, Direction.RIGHT]
        self.__side = random.choice(directions)

    def set_side(self, side):
        self.__side = side

    def _can_shot(self, time):
        return time - self._last_shot >= Normal_Egg.get_cool_time()

    def get_movement_info(self):
        return self.__min_x, self.__max_x, self.__side


class Circle_Chicken(ABS_Chicken):
    def __init__(self, pos: tuple[int, int]):
        img = transform.scale(get_image("chicken"), (100, 100))
        speeed = 2
        super().__init__(img, pos, 2, speeed, in_a_circle, Direction.DOWN, Egg_Types.Normal, 5)
        self.__center = pos
        self.__radios = 200
        self.__index = 0
        self.__on_circle = False
        self.__points = calculate_points(self.__radios, speeed, pos)

    def set_on_circle(self):
        self.__on_circle = True

    def move_index(self):
        n_i = self.__index + 1
        if n_i >= len(self.__points):
            n_i -= len(self.__points)
        self.__index = n_i
        return n_i

    def _can_shot(self, time):
        return time - self._last_shot >= Normal_Egg.get_cool_time()

    def get_on_circle(self):
        return self.__on_circle, self.__points, self.__index, self.__radios, self.__center
