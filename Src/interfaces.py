import abc
from typing import Optional

from pygame import Surface


class i_Renderable(abc.ABC):
    def __init__(self, game, img: Optional[Surface], pos: tuple[int, int], draw_func=None):
        self._img: Surface = img
        self._pos: tuple[int, int] = pos
        self._draw_func = draw_func
        game.add_render(self)

    def get_pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = (x, y)

    def render(self, screen: Surface):
        if self._img:
            screen.blit(self._img, self._pos)
        else:
            self._draw_func(screen)


class i_MoveAble(abc.ABC):
    def __init__(self, game, func):
        self._move_func = func
        game.add_move(self)

    def move(self):
        self._move_func(self)


class i_Damages(abc.ABC,i_MoveAble):
    def __init__(self, game, damage, pos):
        self._damage = damage
        self._pos = pos
        game.add_to_damages(self)

    def get_info(self):
        return self._pos, self._damage


class i_Decidable(abc.ABC):
    def __init__(self, game, pos, size, hp):
        self._pos = pos
        self._size = size
        self._hp = hp
        game.add_decidable(self)
        self.game = game

    def hit(self, h_pos: tuple[int, int]) -> bool:
        x_h, y_h = h_pos
        x, y = self._pos
        w, h = self._size
        return x <= x_h <= x + w and y <= y_h <= y + h

    def collide(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self.game.remove_from_game(self)
