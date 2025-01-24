from dataclasses import dataclass
from typing import Any
from .enums import Dir
from logger import *


@dataclass
class Node:
    name: str

    up: Any = None
    right: Any = None
    down: Any = None
    left: Any = None

    min: int = -1

    up_dir: int = 1
    right_dir: int = 1
    down_dir: int = 1
    left_dir: int = 1

    dir: Dir = Dir.none

    def get_node(self, name: str) -> Any | None:
        if len(name) < 2:
            return None

        symbol = int(name[0])
        num = int(name[1])
        self_symbol = int(self.name[0])
        self_num = int(self.name[1])

        if not (1 <= symbol <= 7) or not (1 <= num <= 5):
            return None

        if self_symbol > symbol:
            if self.left is None:
                return None
            return self.left.get_node(name)
        if self_symbol < symbol:
            if self.right is None:
                return None
            return self.right.get_node(name)
        
        if self_num > num:
            if self.up is None:
                return None
            return self.up.get_node(name)
        if self_num < num:
            if self.down is None:
                return None
            return self.down.get_node(name)
        return self

    def __str__(self) -> str:
        return self.name
