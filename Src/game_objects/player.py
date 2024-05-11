from pygame import transform, Surface

from Src.CONST import WIDTH, HEIGHT
from Src.movement import get_Movement, Direction
from Src.game_objects.shots import *
from Src.utils import get_image, movement_func
from Src.interfaces import i_Renderable, i_Decidable


class Player(i_Renderable, i_Decidable):
    def __init__(self, game, size):
        self.game = game
        pos = (WIDTH // 2 - 50, HEIGHT - 150)
        self._img = transform.rotate(transform.scale(get_image("player_ship"), size), 90)
        i_Renderable.__init__(self, game, self._img,
                              pos)
        self.__speed = 5
        i_Decidable.__init__(self, game, pos, size, 3)
        self.__shots: list[abs_Shot] = []
        self.__width = self._img.get_width()
        self.__shot = NormalShoot
        self.__side = Direction.LEFT

    def get_size(self):
        return self._size

    def set_side(self, side):
        self.__side = side

    def render(self, screen: Surface):
        super().render(screen)

    def move(self, keys):
        player_move(self, keys)

    def get_speed(self):
        return self.__speed

    def get_pos(self):
        return self._pos

    def get_side(self):
        return self.__side

    def shoot(self, frame):
        if not self.__shot.can_shot(frame):
            return
        x, y = self._pos
        shot = self.__shot(self.game, (x + self.__width // 2, y - 5), frame, Direction.UP)
        self.__shots.append(shot)


@movement_func
def player_move(x, y, speed, obj: Player, keys: tuple[bool]):
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
            obj._img = transform.flip(obj._img, 1, 0)
        obj.set_side(Direction.RIGHT)
        x += speed
    return x, y
