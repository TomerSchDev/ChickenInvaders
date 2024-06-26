import sys
from Src.CONST import LogLevels
from Src.setting import get_setting
from Src.game import get_game
from Src.level import *
from Src.CONST import SettingOptions,LOGGER
import logging


def init_program():
    args = sys.argv
    setting = get_setting()
    if "-m" in args:
        setting[SettingOptions.Music] = False
    else:
        setting[SettingOptions.Music] = True
    logger = logging.getLogger(LOGGER)  # Create file handlers for different log levels
    debug_handler = logging.FileHandler('game_debug.log')
    debug_handler.setLevel(logging.DEBUG)

    info_handler = logging.FileHandler('game_info.log')
    info_handler.setLevel(logging.INFO)

    warning_handler = logging.FileHandler('game_warning.log')
    warning_handler.setLevel(logging.WARNING)

    error_handler = logging.FileHandler('game_error.log')
    error_handler.setLevel(logging.ERROR)

    # Create formatter
    formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')

    # Set formatter for each handler
    debug_handler.setFormatter(formatter)
    info_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    # Attach handlers to logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)
    levels=[]
    if "-e" in args:
        levels.append(Endless_lvl(1))
    else:
        levels.append(Test_level_circle())
    return levels


def main():
    lvls=init_program()
    g = get_game(lvls)
    g.start()


if __name__ == "__main__":
    main()
