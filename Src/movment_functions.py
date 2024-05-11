from Src.movement import Direction
from Src.utils import movement_func


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
