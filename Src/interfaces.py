import abc
from typing import Optional
import random

from Src.CONST import HEIGHT, WIDTH
from Src.movement import Direction
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


class i_Shooter(abc.ABC):
    def __init__(self, game, direction, shot_type, rnd_shot):
        self._shot_dir = direction
        self._shot = shot_type
        self._rnd_shot = rnd_shot
        self._shots = []
        game.add_shooter(self)

    def shot(self, game, frame):
        if not self._shot._can_shot(frame):
            return
        chance = random.randint(0, 100)
        if chance < self._rnd_shot:
            x, y = self._pos
            w, h = self._size
            x += + w / 2
            y += (h + 5) if self._shot_dir == Direction.DOWN else -5
            shot = self._shot(game, (x, y), frame, self._shot_dir)
            self._shots.append(shot)


class i_MoveAble(abc.ABC):
    def __init__(self, game, func, speed):
        self._move_func = func
        game.add_move(self)
        self._speed = speed

    def move(self):
        self._move_func(self)

    def get_speed(self):
        return self._speed


class i_Damages(i_MoveAble):
    def __init__(self, game, move_func, speed, damage, pos, direction):
        i_MoveAble.__init__(self, game, move_func, speed)
        self._damage = damage
        self._pos = pos
        self._direction = direction
        game.add_to_damages(self)

    def get_info(self):
        return self._pos, self._damage

    def going_outside(self):
        x, y = self._pos
        w, h = self._size
        if self._direction == Direction.UP and y <= 0:
            return True
        if self._direction == Direction.LEFT and x <= 0:
            return True
        if self._direction == Direction.DOWN and y >= HEIGHT - h:
            return True
        if self._direction == Direction.UP and x >= WIDTH - w:
            return True
        return False


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
            return True
        return False
