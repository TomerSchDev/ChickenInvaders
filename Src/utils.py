import pygame
from Src.CONST import WIDTH, HEIGHT

global __game


def get_image(image_name):
    IMAGES_DIR = "./Images/"
    image_path: str = IMAGES_DIR + image_name + ".png"
    return pygame.Surface.convert_alpha(pygame.image.load(image_path))


def movement_func(func):
    def wrapper(obj, *args, **kwargs):
        x, y = obj.get_pos()
        x, y = func(obj, x, y, *args, **kwargs)
        w, h = obj.get_size()
        x = max(min(WIDTH - w, x), 0)
        y = max(min(HEIGHT - h, y), 0)
        obj.set_pos(x, y)

    return wrapper
