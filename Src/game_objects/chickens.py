from typing import Optional

from pygame import Surface, transform
from abc import ABC
from Src.game_objects.egg import *
from Src.utils import get_image
from Src.movement import Direction
from Src.interfaces import i_Renderable, i_MoveAble, i_Decidable, i_Shooter
from Src.movment_functions import in_a_line
import random


class ABS_Chicken(i_Renderable, i_MoveAble, i_Decidable, i_Shooter):
    def __init__(self, game, img: Optional[Surface], pos: tuple[int, int], hp: int, speed, func_m, dir,egg_type,rnd_shot):
        self._size = img.get_size() if img else (0, 0)
        i_Renderable.__init__(self, game, img, pos)
        i_MoveAble.__init__(self, game, func_m, speed)
        i_Decidable.__init__(self, game, pos, self._size, hp)
        i_Shooter.__init__(self,game,dir,egg_type,rnd_shot)


class Normal_Chicken(ABS_Chicken, ABC):
    def __init__(self, game, pos: tuple[int, int]):
        img = transform.scale(get_image("chicken"), (100, 100))
        super().__init__(game, img, pos, 2, 2, in_a_line, Direction.DOWN,Normal_Egg,30)
        x, y = pos
        self.__speed = 2
        self.__min_x = x - 100
        self.__max_x = x + 100
        directions = [Direction.LEFT, Direction.RIGHT]
        self.__side = random.choice(directions)

    def set_side(self, side):
        self.__side = side

    def get_movement_info(self):
        return self.__min_x, self.__max_x, self.__side

    def get_size(self):
        return self._size
