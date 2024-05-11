import pygame

from Src.CONST import HEIGHT, WIDTH
from Src.interfaces import i_Renderable, i_Damages
from Src.movement import Direction
from Src.movment_functions import straight_line_movement


def _update_frame(frame):
    abs_Egg._last_shot = frame


class abs_Egg(i_Renderable, i_Damages):
    _last_shot = -1

    def __init__(self, game, pos: tuple[int, int], damage: int, draw_func, dire: Direction, func_move, speed: int,
                 size: tuple[int, int]):
        self._direction: Direction = dire
        self._size: tuple[int, int] = size
        i_Renderable.__init__(self, game, None, pos, draw_func)
        i_Damages.__init__(self, game, func_move, speed, damage, pos, dire)

    def get_size(self):
        return self._size

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

    def get_direction(self):
        return self._direction


class Normal_Egg(abs_Egg):
    __COOLDOWN = 60  # cool down of 20 frames between each frames

    def __init__(self, game, pos, frame, dire):
        abs_Egg.__init__(self, game, pos, 2, self.draw, dire, straight_line_movement, 10, (20, 20))
        _update_frame(frame)

    @classmethod
    def _can_shot(cls, time):
        return time - cls._last_shot >= cls.__COOLDOWN

    def draw(self, screen: pygame.Surface):
        x, y = self._pos
        width, height = self._size
        r = (width + height) / 2
        pygame.draw.circle(screen, (255, 255, 255), (x + width / 2, y - height / 2), r)
