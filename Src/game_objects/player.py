from pygame import transform, Surface

from Src.CONST import WIDTH, HEIGHT, Direction
from Src.utils import get_image, movement_func, get_Movement
from Src.interfaces import i_Renderable, i_Detectable
from Src.game_objects.shots import abs_Shot


class Player(i_Renderable, i_Detectable):
    def __init__(self, size):
        pos = (WIDTH // 2 - 50, HEIGHT - 150)
        self._img = transform.rotate(transform.scale(get_image("player_ship"), size), 90)
        i_Renderable.__init__(self, self._img,
                              pos)
        self.__speed = 5
        i_Detectable.__init__(self, pos, size, 3,abs_Shot)
        self.__width = self._img.get_width()
        self.__shot = "Normal"
        self.__side = Direction.LEFT
        self._cooldown=20
        self._last_shot=-1

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
        if not self.can_shot(frame):
            return
        x, y = self._pos
        self._last_shot=frame
        return "Shoot",self.__shot,(x + self.__width // 2, y - 5), Direction.UP

    def can_shot(self, frame):
        return frame - self._last_shot >= self._cooldown


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
