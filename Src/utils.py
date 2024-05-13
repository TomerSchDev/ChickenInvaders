import pygame
from Src.CONST import WIDTH, HEIGHT, Direction
from pygame import constants
import math




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


def calculate_dis_to_endScreen(radios, center):
    x, y = center
    possibilities = [x, y, WIDTH - x, HEIGHT - y]
    for p in possibilities:
        radios = min(p, radios)
    return radios


def calculate_points(radius, speeed, center):
    number_of_points = 6 * radius // (speeed * 3)
    radius = calculate_dis_to_endScreen(radius, center)
    angle_per_point = 360 / number_of_points
    points = []
    for index in range(number_of_points):
        angle = math.radians(angle_per_point * index + 90)
        x = math.floor(center[0] + (radius * math.cos(angle)))
        y = math.floor(center[1] + (radius * math.sin(angle)))
        points.append((x, y))
    return points
