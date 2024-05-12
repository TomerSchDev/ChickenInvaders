import pygame
from Src.CONST import WIDTH, HEIGHT, Direction
from pygame import constants

global __game


def get_image(image_name):
    IMAGES_DIR = "./Images/"
    image_path: str = IMAGES_DIR + image_name + ".png"
    return pygame.Surface.convert_alpha(pygame.image.load(image_path))


def get_Movement(keys: tuple[bool]):
    UP = (Direction.UP, constants.K_UP, constants.K_w)
    LEFT = (Direction.LEFT, constants.K_LEFT, constants.K_a)
    DOWN = (Direction.DOWN, constants.K_DOWN, constants.K_s)
    RIGHT = (Direction.RIGHT, constants.K_RIGHT, constants.K_d)
    directions = [UP, LEFT, DOWN, RIGHT]
    movement = {}
    for direction in directions:
        e, a, b = direction
        if keys[a] or keys[b]:
            movement[e] = True
    return movement


def movement_func(func):
    def wrapper(obj, *args, **kwargs):
        x, y = obj.get_pos()
        speed = obj.get_speed()
        x, y = func(x, y, speed, obj, *args, **kwargs)
        w, h = obj.get_size()
        x = max(min(WIDTH - w, x), 0)
        y = max(min(HEIGHT - h, y), 0)
        obj.set_pos(x, y)

    return wrapper


def game_sign(func):
    def wrapper(game, obj_type, obj_sub_type, *args, **kwargs):
        obj = func(obj_type, obj_sub_type, *args, **kwargs)
        game.add_to_game(obj)
        return obj

    return wrapper
