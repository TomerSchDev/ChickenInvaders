from Src.game import get_game
from Src.level import tmp_lvl

import logging
def main():
    logging.basicConfig(filename='game.log', encoding='utf-8',format='%(levelname)s : %(asctime)s : %(message)s', level=logging.DEBUG,datefmt='%y/%m/%d %I:%M:%S %p')
    g = get_game()
    g.init_level(tmp_lvl())
    g.start()


if __name__ == "__main__":
    main()
