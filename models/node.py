from dataclasses import dataclass
from typing import Any
from .enums import Dir


@dataclass
class Node:
    name: int

    up: Any = None
    right: Any = None
    down: Any = None
    left: Any = None

    min: int = -1

    up_dir: int = -1
    right_dir: int = -1
    down_dir: int = -1
    left_dir: int = -1

    dir: Dir = Dir.none
