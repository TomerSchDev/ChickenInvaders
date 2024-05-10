from abc import ABC
from Src.interfaces import i_Renderable,i_MoveAble,i_Damages
class abs_Egg(ABC,i_Renderable,i_MoveAble,i_Damages):
    pass
