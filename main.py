from Src.game import get_game
from Src.level import tmp_lvl

def main():

    g = get_game()
    g.init_level(tmp_lvl())
    g.start()


if __name__ == "__main__":
    main()
