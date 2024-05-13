import pygame

from Src.interfaces import i_Renderable, i_Damages
from Src.movment_functions import straight_line_movement


def _update_frame(frame):
    abs_Egg._last_shot = frame


class abs_Egg(i_Renderable, i_Damages):
    _last_shot = -1

    def __init__(self, pos: tuple[int, int], damage: int, draw_func, dire, func_move, speed: int,
                 size: tuple[int, int]):
        self._direction = dire
        i_Renderable.__init__(self, None, pos, draw_func)
        i_Damages.__init__(self, func_move, speed, damage, pos, dire,size)


    def get_direction(self):
        return self._direction


class Normal_Egg(abs_Egg):
    __COOLDOWN = 60  # cool down of 20 frames between each frames

    def __init__(self, pos, frame, dire):
        abs_Egg.__init__(self, pos, 2, self.draw, dire, straight_line_movement, 10, (20, 20))
        _update_frame(frame)

    @classmethod
    def get_cool_time(cls):
        return cls.__COOLDOWN

    def draw(self, screen: pygame.Surface):
        x, y = self._pos
        width, height = self._size
        r = (width + height) / 2
        pygame.draw.circle(screen, (255, 255, 255), (x + width / 2, y - height / 2), r)
