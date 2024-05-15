from Src.creatables.chickens import *
from Src.creatables.player import Player
from Src.creatables.shots import *
from Src.creatables.egg import *
from Src.utils import play_music, get_sound

"""
Object dic

every object type that can be created is store here
"""
objects_dic = {
    Enemy_Typs.NORMAL: Normal_Chicken,
    Enemy_Typs.CIRCLE: Circle_Chicken,
    Egg_Types.Normal: Normal_Egg,
    PLAYER: Player,
    Shoot_Typs.NORMAl: (NormalShoot, get_sound("lazer_shot")),
    Shoot_Typs.ANGLE: (Angle_Shoot, get_sound("lazer_shot")),
    Shoot_Typs.THREE_ANGLE: [Three_Angle_Shoot],
    Shoot_Typs.FIVE_ANGE: [Five_Angle_Shoot]

}


def create_object(game, t, *args, **kwargs):
    if t not in objects_dic:
        raise ValueError(f"Type {t} not supported")
    ot = objects_dic[t]
    if isinstance(ot, tuple):
        ot, music_file = ot
        play_music(music_file)
    if isinstance(ot, list):
        to_create = ot[0].create(*args)
        ret = []
        for nt, arg in to_create:
            ret.append(create_object(game, nt, *arg, **kwargs))
        return ret
    obj = ot(*args, **kwargs)
    game.add_to_game(obj)
    return obj
