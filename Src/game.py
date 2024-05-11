import pygame
from Src.CONST import *
from Src.game_objects.player import Player
from Src.game_objects.chickens import *

__game = None


def get_game():
    global __game
    if __game is None:
        __game = __Game()
    return __game


class __Game:


    def __init__(self):

        self.__demesnes = []
        self.__renderAbles = []
        self.__moveAbles = []
        self.__seen = []
        self.__shooters = []
        self.window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.transform.scale(get_image("background"), (WIDTH, HEIGHT))
        self.window.blit(self.background, (0, 0))
        self.__game_objects = [self.__demesnes, self.__renderAbles, self.__moveAbles, self.__seen, self.__shooters]

    def add_shooter(self, shooter):
        self.__shooters.append(shooter)

    def render(self):
        screen: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for r in self.__renderAbles:
            r.render(screen)
        self.window.blit(self.background, (0, 0))
        self.window.blit(screen, (0, 0))
        pygame.display.flip()

    def move(self):
        for m in self.__moveAbles:
            m.move()

    def check_hit(self):
        for d in self.__demesnes:
            pos, damage = d.get_info()
            for s in self.__seen:
                if s.hit(pos):
                    s.collide(damage)

    def add_render(self, render):
        self.__renderAbles.append(render)

    def add_move(self, movable):
        self.__moveAbles.append(movable)

    def add_decidable(self, d):
        self.__seen.append(d)

    def remove_from_game(self, o):
        for arr in self.__game_objects:
            if o in arr:
                arr.remove(o)

    def add_to_damages(self, d):
        self.__demesnes.append(d)

    def check_if_in_game(self, obj):
        return obj in self.__seen or obj in self.__moveAbles or obj in self.__renderAbles

    def start(self):
        run_game = True
        player = Player(self, (100, 100))
        clock = pygame.time.Clock()
        frame = 0
        Normal_Chicken(self, (200, 200))
        while run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
            keys: tuple[bool] = pygame.key.get_pressed()
            if any(keys):
                if keys[pygame.K_ESCAPE]:
                    run_game = False
                if keys[pygame.K_LALT]:
                    debug = 1
                player.move(keys)
                if keys[pygame.K_SPACE]:
                    player.shoot(frame)
            self.update(frame)

            if not self.check_if_in_game(player):
                run_game = False
            frame += 1
            clock.tick(FPS)

    def shot(self, frame):
        for s in self.__shooters:
            s.shot(self, frame)

    def check_is_outside(self):
        for d in self.__demesnes:
            if d.going_outside():
                self.remove_from_game(d)

    def update(self, frame):
        self.shot(frame)
        self.move()
        self.check_hit()
        self.check_is_outside()
        self.render()
