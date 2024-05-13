import abc
from Src.interfaces import i_Renderable, i_Damages
from Src.movment_functions import straight_line_movement
import pygame


def _update_frame(frame):
    abs_Shot._last_shot = frame


class abs_Shot(i_Renderable, i_Damages):
    _last_shot = -1

    def __init__(self, pos: tuple[int, int], damage: int, draw_func, dire, func_move, speed,size):
        self._size = size
        i_Renderable.__init__(self, None, pos, draw_func)
        i_Damages.__init__(self, func_move, speed, damage, pos,dire)

    def get_size(self):
        return self._size



    def get_direction(self):
        return self._direction


class NormalShoot(abs_Shot):
    __COOLDOWN = 20  # cool down of 20 frames between each frames

    def __init__(self, pos, dire):
        abs_Shot.__init__(self, pos, 2, self.draw, dire, straight_line_movement, 10,(20, 20))

    def draw(self, screen: pygame.Surface):
        x, y = self._pos
        width, height = self._size
        pygame.draw.rect(screen, (255, 0, 0, 150), (x, y - height, width, height))
    @classmethod
    def get_cool_down(cls):
        return cls.__COOLDOWN