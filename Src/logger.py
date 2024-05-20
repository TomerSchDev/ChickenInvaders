from __future__ import annotations

import inspect
import logging
import re
from Src.CONST import LogLevels,LOGGER

logger = logging.getLogger(LOGGER)

CLASS_NAME = "{INSERT_CLASS_HERE}"

len_insert = len(CLASS_NAME)


def replace_message(message: str, insert: str):
    index = message.find(CLASS_NAME)
    return message[:index] + insert + " " + message[index + len_insert + 1:]


def __write_log(lvl, message: str):
    caller = inspect.stack()[2][3]
    lvl(caller+":"+message)


def __get_message(message :str|tuple):
    arg_number = -1 if isinstance(message,str) else len(message)
    if arg_number == 2:  # mean class name + message
        message = debug_class(message[0], message[1])
    return message


def log(lvl: LogLevels, message):
    write_message = __get_message(message)
    __write_log(lvl, write_message)


def debug_class(cls, message: str) -> str:
    cls_name: str = str(cls).split(".")[-1]
    cls_name_parte = re.sub(r'(?<!^)(?=[A-Z])', ' ', cls_name)
    return replace_message(message, cls_name_parte)
