from time import gmtime, strftime
from pprint import pprint
from typing import Any


def log(msg: Any):
    print(f"\033[32m[{strftime('%H:%M:%S', gmtime())}] LOG:", end="\033[37m ")
    if type(msg) == str:
        print(msg)
    else:
        pprint(msg)


def error(msg: Any):
    print(f"\033[31m[{strftime('%H:%M:%S', gmtime())}] ERROR:", end="\033[37m ")
    if type(msg) == str:
        print(msg)
    else:
        pprint(msg)
