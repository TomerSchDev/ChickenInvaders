from Src.CONST import Direction
from Src.utils import movement_func

import math


@movement_func
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


@movement_func
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


@movement_func
def in_a_circle(x, y, speed, obj):
    on_the_circle, points, index, radios, center = obj.get_on_circle()
    if obj.point_inside(points[index]):
        index = obj.move_index()

    w, h = obj.get_size()
    cx = x + w // 2
    cy = y + h // 2
    if on_the_circle:
        px, py = points[index]
        y_speed = min(speed, math.fabs(py - cy))
        ny = (y + y_speed) if (py - cy) > 0 else (y - y_speed)
        x_speed = min(speed, math.fabs(px - cx))
        nx = (x + x_speed) if (px - cx) > 0 else (x - x_speed)
        return nx, ny
    c_x, c_y = center
    n_x = cx + speed
    c_r = math.floor(math.sqrt((cx - c_x) ** 2 + (cy - c_y) ** 2))
    if c_r - radios < 2:
        obj.set_on_circle()
    return n_x, y
