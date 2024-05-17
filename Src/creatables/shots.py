from Src.CONST import Shoot_Typs
from Src.utils import created_rays_in_angle, add_damage
from Src.interfaces import i_Renderable, i_Damages
from Src.movment_functions import straight_line_movement, rays_in_a_angle
import pygame


def _update_frame(frame):
    abs_Shot._last_shot = frame


class abs_Shot(i_Renderable, i_Damages):
    _last_shot = -1

    def __init__(self, pos: tuple[int, int], damage: int, draw_func, dire, func_move, speed, size):
        i_Renderable.__init__(self, None, pos, draw_func)
        i_Damages.__init__(self, func_move, speed, damage, pos, dire, size, add_damage)

    def get_direction(self):
        return self._direction


class NormalShoot(abs_Shot):
    __COOLDOWN = 20  # cool down of 20 frames between each frames

    def __init__(self, pos, dire):
        abs_Shot.__init__(self, pos, 2, self.draw, dire, straight_line_movement, 10, (20, 20))

    def draw(self, screen: pygame.Surface):
        x, y = self._pos
        width, height = self._size
        pygame.draw.rect(screen, (255, 0, 0, 150), (x, y - height, width, height))

    @classmethod
    def get_cool_down(cls):
        return cls.__COOLDOWN


class Angle_Shoot(abs_Shot):
    __COOLDOWN = 40  # cool down of 40 frames between each frames

    def __init__(self, pos, dire, angle):
        abs_Shot.__init__(self, pos, 2, self.draw, dire, rays_in_a_angle, 10, (10, 10))
        self.__angle = angle

    def get_angle(self):
        return self.__angle

    def draw(self, screen: pygame.Surface):
        width, height = self._size
        pygame.draw.circle(screen, (255, 0, 0, 150), self._pos, width)

    @classmethod
    def get_cool_down(cls):
        return cls.__COOLDOWN


class Three_Angle_Shoot:
    @staticmethod
    def create(pos, dir):
        angles = created_rays_in_angle(3, dir)
        ret = []
        for angle in angles:
            ret.append((Shoot_Typs.ANGLE, (pos, dir, angle)))
        return ret


class Five_Angle_Shoot:
    @staticmethod
    def create(pos, dir):
        angles = created_rays_in_angle(5, dir)
        ret = []
        for angle in angles:
            ret.append((Shoot_Typs.ANGLE, (pos, dir, angle)))
        return ret
