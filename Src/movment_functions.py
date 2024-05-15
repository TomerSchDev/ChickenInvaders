from Src.CONST import Direction
from Src.utils import get_angle_from_point
import math


def straight_line_movement(x, y, speed, obj):
    direction = obj.get_direction()
    if direction == Direction.UP:
        y -= speed
    elif direction == Direction.DOWN:
        y += speed
    elif direction == Direction.RIGHT:
        x += speed
    elif direction == Direction.LEFT:
        x -= speed
    return x, y


def in_a_line(x, y, speed, obj):
    min_x, max_x, direction = obj.get_movement_info()
    if direction == Direction.RIGHT:
        x += speed
    else:
        x -= speed
    if x >= max_x:
        obj.set_side(Direction.LEFT)
    elif x <= min_x:
        obj.set_side(Direction.RIGHT)
    return x, y


def in_a_circle(x, y, speed, obj):
    on_the_circle, points, index, radios, center = obj.get_on_circle()
    if obj.point_inside(points[index]):
        index = obj.move_index()

    w, h = obj.get_size()
    cx = x + w // 2
    cy = y + h // 2
    if on_the_circle:
        target = points[index]
        base = (cx,cy)
        angle_to_move_r = get_angle_from_point(base, target)
        nx = math.floor(x + (speed * math.cos(angle_to_move_r)))
        ny = math.floor(y + (speed * math.sin(angle_to_move_r)))
        return nx, ny
    c_x, c_y = center
    n_x = cx + speed
    c_r = math.floor(math.sqrt((cx - c_x) ** 2 + (cy - c_y) ** 2))
    if c_r - radios < 2:
        obj.set_on_circle()
    return n_x, y


def rays_in_a_angle(x, y, speed, obj):
    angle = obj.get_angle()
    nx = math.floor(x + (speed * math.cos(angle)))
    ny = math.floor(y + (speed * math.sin(angle)))
    return nx, ny
