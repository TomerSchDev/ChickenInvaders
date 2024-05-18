import sys

from Src.setting import get_setting
from Src.game import get_game
from Src.level import tmp_lvl
from Src.CONST import SettingOptions
import logging


def main():
    args = sys.argv
    setting = get_setting()
    if "-m" in args:
        setting[SettingOptions.Music] = False
    else:
        setting[SettingOptions.Music] = True

    logging.basicConfig(filename='game.log', encoding='utf-8', format='%(levelname)s : %(asctime)s : %(message)s',
                        level=logging.DEBUG, datefmt='%y/%m/%d %I:%M:%S %p')
    g = get_game(setting)
    g.init_level(tmp_lvl())
    g.start()


if __name__ == "__main__":
    main()
