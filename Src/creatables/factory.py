from Src.CONST import *
from Src.creatables.chickens import *
from Src.creatables.player import Player
from Src.creatables.shots import *
from Src.creatables.egg import *

objects_dic = {
    Enemy_Typs.NORMAL: Normal_Chicken,
    Enemy_Typs.CIRCLE: Circle_Chicken,
    Egg_Types.Normal: Normal_Egg,
    PLAYER: Player,
    Shoot_Typs.NORMAl: NormalShoot
}


def create_object(game, t, *args, **kwargs):
    obj = objects_dic[t](*args, **kwargs)
    game.add_to_game(obj)
    return obj
