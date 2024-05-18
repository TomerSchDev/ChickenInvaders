from Src.logger import log
from Src.CONST import LogLevels


def validate(value):
    if not isinstance(value, bool):
        raise ValueError(f"Value {value} must be a boolean")


setting = None


def get_setting():
    global setting
    if setting is None:
        setting = __Setting()
    return setting


class __Setting:
    def __init__(self):
        self.__settings = {}

    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        self.set_value(key, value)

    def __delitem__(self, key):
        if key in self.__dict__:
            del self.__settings[key]

    def __contains__(self, key):
        return key in self.__settings

    def __add_setting(self, name, value=False):
        self.__settings[name] = value

    def set_value(self, name, value):
        try:
            validate(value)
        except ValueError as e:
            log(LogLevels.ERROR, e)
            return
        if name in self.__settings:
            self.__settings[name] = value
        else:
            self.__add_setting(name, value)

    def get_value(self, name):
        if name in self.__settings:
            return self.__settings[name]
        else:
            raise KeyError(f"Setting '{name}' not found")

    def toggle(self, name):
        if name in self.__settings:
            self.__settings[name] = not self.__settings[name]
        else:
            raise KeyError(f"Setting '{name}' not found")

    def __str__(self):
        return f"Settings({self.__settings})"

    def __repr__(self):
        return self.__str__()
