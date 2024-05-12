from abc import ABC
import random
from Src.CONST import WIDTH, HEIGHT


class Chicken_Info:
    def __init__(self, c_type, pos):
        self.c_type = c_type
        self.pos = pos

    def get_info(self):
        return self.c_type, self.pos


class abs_Level(ABC):
    def __init__(self, chickens: list[Chicken_Info]):
        self.chickens_info = chickens


def create_chickens_demo(count) -> list[Chicken_Info]:
    res =[]
    for _ in range(count):
        x = random.randint(0, WIDTH - 100)
        y = random.randint(0, HEIGHT - 100)
        pos = (x,y)
        res.append(Chicken_Info("Normal",pos))
    return res


class tmp_lvl(abs_Level):
    def __init__(self):
        chickens = create_chickens_demo(10)
        super().__init__(chickens)
