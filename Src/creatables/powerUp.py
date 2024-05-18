from Src.interfaces import *
from Src.utils import get_image
from Src.movment_functions import straight_line_movement
from Src.CONST import Direction


def add_upgrade(give,obj):
    obj.upgrade()
    return False


class PowerUp(i_Renderable, i_Damages):
    def __init__(self, pos: tuple[int, int]):
        size = (30, 30)
        img = get_image("gift", size)
        i_Renderable.__init__(self, img, pos)
        i_Damages.__init__(self, straight_line_movement, 2, 0, pos, Direction.DOWN, size, action_func=add_upgrade)