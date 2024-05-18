from pygame import transform, key

from Src.CONST import *
from Src.utils import get_image, get_Movement
from Src.interfaces import i_Renderable, i_Detectable, i_MoveAble
from Src.creatables.shots import abs_Shot


def player_move(x, y, speed, obj):
    keys = key.get_pressed()
    movements = get_Movement(keys)
    side = obj.get_side()
    if movements.get(Direction.UP):
        y -= speed
    if movements.get(Direction.DOWN):
        y += speed
    if movements.get(Direction.LEFT):
        if side != Direction.LEFT:
            obj._img = transform.flip(obj._img, 1, 0)
        obj.set_side(Direction.LEFT)
        x -= speed
    if movements.get(Direction.RIGHT):
        if side != Direction.RIGHT:
            obj._img = transform.flip(obj.img, 1, 0)
        obj.set_side(Direction.RIGHT)
        x += speed
    return x, y


class Player(i_Renderable, i_Detectable, i_MoveAble):
    def __init__(self, size):
        pos = (WIDTH // 2 - 50, HEIGHT - 150)
        self._img = transform.rotate(get_image("player_ship", size), 90)
        i_Renderable.__init__(self, self._img,
                              pos)
        i_MoveAble.__init__(self, player_move, 5, pos, size)
        i_Detectable.__init__(self, pos, size, 3, [abs_Shot], 0, self.empty)
        self.__width = self._img.get_width()
        self.__shot = Shoot_Typs.NORMAl
        self.__side = Direction.LEFT
        self._cooldown = 20
        self._last_shot = -1
        self.__name__="Player"
    def empty(self):
        return None
    def upgrade(self):
        if self.__shot == Shoot_Typs.THREE_ANGLE:
            self.__shot = Shoot_Typs.FIVE_ANGE
        if self.__shot == Shoot_Typs.NORMAl:
            self.__shot = Shoot_Typs.THREE_ANGLE

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side


    def shoot(self, frame):
        if not self.can_shot(frame):
            return
        x, y = self._pos
        self._last_shot = frame
        return self.__shot, (x + self.__width // 2, y - 5), Direction.UP

    def can_shot(self, frame):
        return frame - self._last_shot >= self._cooldown

    @property
    def img(self):
        return self._img
