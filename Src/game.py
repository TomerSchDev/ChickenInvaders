import pygame
from Src.CONST import *
from Src.creatables.player import Player
from Src.creatables.factory import create_object
from Src.utils import get_image
from Src.level import abs_Level

__game = None


def get_game():
    global __game
    if __game is None:
        __game = __Game()
    return __game


class __Game:

    def __init__(self):
        self.window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = get_image("background", (WIDTH, HEIGHT))
        self.window.blit(self.background, (0, 0))
        self.__game_objects = {obj: [] for obj in Objects_Type}
        self.player = None
        self.__lvl_loaded = False
        pygame.mixer.init()

    def init_level(self, lvl: abs_Level):
        self.player = create_object(self, PLAYER, (100, 100))
        for c_i in lvl.chickens_info:
            create_object(self, *c_i.get_info())
        self.__lvl_loaded = True

    def render(self):
        screen: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for r in self.__game_objects[Objects_Type.RENDER_ABLE]:
            r.render(screen)
        self.window.blit(self.background, (0, 0))
        self.window.blit(screen, (0, 0))
        pygame.display.flip()

    def move(self):
        for m in self.__game_objects[Objects_Type.MOVE_ABLE]:
            m.move()

    def check_hit(self):
        for d in self.__game_objects[Objects_Type.DAMAGE_ABLE]:
            pos, damage = d.get_info()
            for s in self.__game_objects[Objects_Type.DETECT_ABLE]:
                if not s.hit(pos, d):
                    continue
                res = d.collide(s)
                self.remove_from_game(d)
                if res is False:
                    continue
                if res is not True:
                    create_object(self, *res)
                self.remove_from_game(s)

    def remove_from_game(self, o):
        for arr in self.__game_objects.values():
            if o in arr:
                arr.remove(o)

    def check_if_in_game(self, obj):
        for arr in self.__game_objects.values():
            if obj in arr:
                return True
        return False

    def start(self):
        if not self.__lvl_loaded:
            return
        run_game = True
        clock = pygame.time.Clock()
        frame = 0
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
                if keys[pygame.K_SPACE]:
                    res = self.player.shoot(frame)
                    if res:
                        create_object(self, *res)
            self.update(frame)
            if not self.check_if_in_game(self.player):
                run_game = False
            frame += 1
            clock.tick(FPS)
        self.unload_lvl()

    def shot(self, frame):
        for s in self.__game_objects[Objects_Type.SHOOTERS]:
            res = s.shot(frame)
            if res:
                create_object(self, *res)

    def check_is_outside(self):
        for d in self.__game_objects[Objects_Type.DAMAGE_ABLE]:
            if d.going_outside():
                self.remove_from_game(d)

    def add_to_game(self, obj):
        obj_types = obj.get_i_types()
        for t in obj_types:
            self.__game_objects[t].append(obj)

    def update(self, frame):
        self.shot(frame)
        self.move()
        self.check_hit()
        self.check_is_outside()
        self.render()

    def unload_lvl(self):
        self.__lvl_loaded = False
        for arr in self.__game_objects.values():
            arr.clear()
        self.player = None
