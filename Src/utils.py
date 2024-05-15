import logging
import inspect
import pygame
from Src.CONST import WIDTH, HEIGHT, Direction
from pygame import constants
import math

IMAGES_DIR = "./Images/"
SOUND_DIR = "./Sounds/"
pygame.mixer.init()
logger = logging.getLogger(__name__)


def debug(message):
    caller=inspect.stack()[1][3]
    logger.debug('%s : %s', caller, message)


def get_sound(sound_name):
    sound_path = SOUND_DIR + sound_name + ".mp3"
    return pygame.mixer.Sound(sound_path)


def play_music(sound_file: pygame.mixer.Sound):
    sound_file.play()


def get_image(image_name):
    image_path: str = IMAGES_DIR + image_name + ".png"
    return pygame.Surface.convert_alpha(pygame.image.load(image_path))


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


"""
    double dx = screenPoint.getX() - mCentreX;
    // Minus to correct for coord re-mapping
    double dy = -(screenPoint.getY() - mCentreY);

    double inRads = Math.atan2(dy, dx);

    // We need to map to coord system when 0 degree is at 3 O'clock, 270 at 12 O'clock
    if (inRads < 0)
        inRads = Math.abs(inRads);
    else
        inRads = 2 * Math.PI - inRads;

"""


def get_angle_from_point(base, target):
    bx, by = base
    tx, ty = target
    dx = tx - bx
    dy = -(ty - by)
    angleRed = math.atan2(dy, dx)
    if angleRed < 0:
        angleRed = math.fabs(angleRed)
    else:
        angleRed = 2 * math.pi - angleRed
    return angleRed


UP = (Direction.UP, constants.K_UP, constants.K_w)
LEFT = (Direction.LEFT, constants.K_LEFT, constants.K_a)
DOWN = (Direction.DOWN, constants.K_DOWN, constants.K_s)
RIGHT = (Direction.RIGHT, constants.K_RIGHT, constants.K_d)
directions = [UP, LEFT, DOWN, RIGHT]


def created_rays_in_angle(rays_count, direction):
    rays = []
    diff_angle = 180 // (rays_count + 1)
    start_angle = -1
    for i, (dir, k1, k2) in enumerate(directions):
        if direction == dir:
            start_angle = i * 90 + 180
            break
    if start_angle == -1:
        debug("unvalid angle")
        return rays
    for i in range(1, rays_count + 1):
        r_angle = start_angle + diff_angle * i
        print(r_angle)
        angle = math.radians(r_angle)
        rays.append(angle)
    debug(f"created {rays}")
    return rays


def get_Movement(keys: tuple[bool]):
    movement = {}
    for direction in directions:
        e, a, b = direction
        if keys[a] or keys[b]:
            movement[e] = True
    return movement
