from pygame import transform, Surface
from Src.movement import get_Movement
from Src.game_objects.shots import *
from Src.utils import get_image
from Src.interfaces import i_Renderable, i_Decidable


class Player(i_Renderable,i_Decidable):
    def __init__(self, game, size):
        self.game = game
        pos = (WIDTH // 2 - 50, HEIGHT - 150)
        self._img = transform.rotate(transform.scale(get_image("player_ship"), size), 90)
        i_Renderable.__init__(self, game, self._img,
                              pos)
        i_Decidable.__init__(self, game, pos, size,3)
        self.__shots: list[abs_Shot] = []
        self.__width = self._img.get_width()
        self.__speed = 5
        self.__shot = NormalShoot
        self.__side = Direction.LEFT

    def get_size(self):
        return self._size

    @movement_func
    def move(self, x, y, keys: tuple[bool]):
        movements = get_Movement(keys)

        if movements[Direction.UP.value]:
            y -= self.__speed
        if movements[Direction.DOWN.value]:
            y += self.__speed
        if movements[Direction.LEFT.value]:
            if self.__side != Direction.LEFT:
                self._img = transform.flip(self._img, 1, 0)
            self.__side = Direction.LEFT
            x -= self.__speed
        if movements[Direction.RIGHT.value]:
            if self.__side != Direction.RIGHT:
                self._img = transform.flip(self._img, 1, 0)
            self.__side = Direction.RIGHT
            x += self.__speed
        return x, y

    def render(self, screen: Surface):
        super().render(screen)
        for shot in self.__shots:
            if shot.going_outside():
                self.game.remove_from_game(shot)
            else:
                shot.move()

    def shoot(self, frame):
        if not self.__shot.can_shot(frame):
            return
        x, y = self._pos
        shot = self.__shot(self.game,(x + self.__width // 2, y - 5), frame, Direction.UP)
        self.__shots.append(shot)
