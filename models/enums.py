from enum import Enum


class Dir(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

    none = 4

    def __str__(self) -> str:
        res = {
            Dir.up: "↑",
            Dir.right: "→",
            Dir.left: "←",
            Dir.down: "↓",
            Dir.none: "-"
        }

        return res[self]
