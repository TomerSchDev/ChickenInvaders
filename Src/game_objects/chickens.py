from typing import Optional

from pygame import Surface, transform
from abc import abstractmethod, ABC
from Src.utils import get_image, movement_func
from Src.movement import Direction
from Src.interfaces import i_Renderable, i_MoveAble, i_Decidable
import random


class ABS_Chicken(i_Renderable, i_MoveAble, i_Decidable):
    def __init__(self, game, img: Optional[Surface], pos: tuple[int, int], hp: int):
        self._size = img.get_size() if img else (0, 0)
        i_Renderable.__init__(self, game, img, pos)
        i_MoveAble.__init__(self, game, self.move)
        i_Decidable.__init__(self, game, pos,self._size, hp)

    @abstractmethod
    def move(self):
        pass


class Normal_Chicken(ABS_Chicken, ABC):
    def __init__(self,game, pos: tuple[int, int]):
        img = transform.scale(get_image("chicken"), (100, 100))
        super().__init__(game,img, pos,2)
        x, y = pos
        self.__speed = 2
        self.__min_x = x - 100
        self.__max_x = x + 100
        directions = [Direction.LEFT, Direction.RIGHT]
        self.__side = random.choice(directions)

    def get_size(self):
        return self._size

    @movement_func
    def move(self, x, y):
        if x > self.__max_x:
            self.__side = Direction.LEFT
        elif x < self.__min_x:
            self.__side = Direction.RIGHT
        if self.__side == Direction.RIGHT:
            x += self.__speed
        else:
            x -= self.__speed
        return x, y
