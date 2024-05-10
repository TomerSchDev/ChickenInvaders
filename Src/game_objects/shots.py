import abc
from Src.interfaces import i_Renderable,i_Damages
from Src.interfaces import i_MoveAble
from Src.utils import movement_func
from Src.movement import Direction
from Src.CONST import WIDTH, HEIGHT
import pygame


def _update_frame(frame):
    abs_Shot._last_shot = frame


class abs_Shot(i_Renderable, i_MoveAble,i_Damages):
    _last_shot = -1

    def __init__(self, game, pos: tuple[int, int], damage: int, draw_func, dire):
        self._direction = dire
        self.__size = (0, 0)
        i_Renderable.__init__(self, game, None, pos, draw_func)
        i_MoveAble.__init__(self, game, self.move)
        i_Damages.__init__(self,game,damage,pos)

    @abc.abstractmethod
    def move(self):
        pass

    def going_outside(self):
        x, y = self._pos
        w, h = self.__size
        if self._direction == Direction.UP and y <= 0:
            return True
        if self._direction == Direction.LEFT and x <= 0:
            return True
        if self._direction == Direction.DOWN and y >= HEIGHT - h:
            return True
        if self._direction == Direction.UP and x >= WIDTH - w:
            return True
        return False


class NormalShoot(abs_Shot):
    __COOLDOWN = 20  # cool down of 20 frames between each frames

    def __init__(self, game, pos, frame, dire):
        self.__size = (20, 20)
        self.__speed = 10
        abs_Shot.__init__(self, game, pos, 2, self.draw, dire)
        _update_frame(frame)

    def draw(self, screen: pygame.Surface):
        x, y = self._pos
        width, height = self.__size
        pygame.draw.rect(screen, (255, 0, 0, 150), (x, y - height, width, height))

    def get_size(self):
        return self.__size

    @movement_func
    def move(self, x, y):
        # currently only going up, need to implement sideways movement
        if self._direction == Direction.UP:
            y -= self.__speed
        elif self._direction == Direction.DOWN:
            y += self.__speed
        elif self._direction == Direction.RIGHT:
            x += self.__speed
        elif self._direction == Direction.LEFT:
            x -= self.__speed

        return x, y

    def add_to_game(self, game):
        game.add_render(self)
        game.add_moveable(self)

    @classmethod
    def can_shot(cls, time):
        return time - cls._last_shot >= cls.__COOLDOWN
