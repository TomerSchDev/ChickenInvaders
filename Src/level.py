from abc import ABC


class abs_Level(ABC):
    def __init__(self,chickens):
        self.chickens = chickens
    def run_level(self):
        pass