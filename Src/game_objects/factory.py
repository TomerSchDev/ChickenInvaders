from Src.utils import game_sign
from Src.game_objects.chickens import *
from Src.game_objects.egg import *
from Src.game_objects.shots import *

objects_dic = {
    "Chicken": {"Normal": Normal_Chicken},
    "Egg": {"Normal": Normal_Egg},
    "Shoot": {"Normal": NormalShoot}
}


@game_sign
def create_object(obj_type, obj_sub_type, *args, **kwargs):
    return objects_dic[obj_type][obj_sub_type](*args, **kwargs)
