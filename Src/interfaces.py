from abc import ABC
from typing import Optional
import random

from Src.CONST import *
from pygame import Surface


class abs_interface(ABC):
    def __init__(self):
        if not hasattr(self, "_o_types"):
            self._o_types = []

    def get_i_types(self):
        return self._o_types


class i_Renderable(abs_interface):
    def __init__(self, img: Optional[Surface], pos: tuple[int, int], draw_func=None):
        self._img: Surface = img
        self._pos: tuple[int, int] = pos
        self._draw_func = draw_func
        abs_interface.__init__(self)
        self._o_types.append(Objects_Type.RENDER_ABLE)

    def get_pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = (x, y)

    def render(self, screen: Surface):
        if self._img:
            screen.blit(self._img, self._pos)
        else:
            self._draw_func(screen)


class i_Shooter(abs_interface):
    def __init__(self, direction, shot_type, rnd_shot):
        abs_interface.__init__(self)
        self._shot_dir = direction
        self._shot = shot_type
        self._rnd_shot = rnd_shot
        self._last_shot=-1
        self._o_types.append(Objects_Type.SHOOTERS)

    def shot(self, frame):
        if not self._can_shot(frame):
            return
        chance = random.randint(0, 100)
        if chance < self._rnd_shot:
            x, y = self._pos
            w, h = self._size
            x += + w / 2
            y += (h + 5) if self._shot_dir == Direction.DOWN else -5
            shot_type, shot_sub_type = self._shot
            self._last_shot = frame
            return shot_type, shot_sub_type, (x, y), frame, self._shot_dir


class i_MoveAble(abs_interface):
    def __init__(self, func, speed):
        abs_interface.__init__(self)
        self._move_func = func
        self._speed = speed
        self._o_types.append(Objects_Type.MOVE_ABLE)

    def move(self):
        self._move_func(self)

    def get_speed(self):
        return self._speed


class i_Damages(i_MoveAble):
    def __init__(self, move_func, speed, damage, pos, direction):
        i_MoveAble.__init__(self, move_func, speed)
        abs_interface.__init__(self)
        self._damage = damage
        self._pos = pos
        self._direction = direction
        self._o_types.append(Objects_Type.DAMAGE_ABLE)

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


class i_Detectable(abs_interface):
    def __init__(self, pos, size, hp):
        abs_interface.__init__(self)
        self._pos = pos
        self._size = size
        self._hp = hp
        self._o_types.append(Objects_Type.DETECT_ABLE)

    def hit(self, h_pos: tuple[int, int]) -> bool:
        x_h, y_h = h_pos
        x, y = self._pos
        w, h = self._size
        return x <= x_h <= x + w and y <= y_h <= y + h

    def collide(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            return True
        return False
