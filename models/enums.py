from enum import Enum


class Dir(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

    none = 4

    @staticmethod
    def relate(n1, n2):
        if n1 == Dir.up:
            if n2 == Dir.right:
                return Dir.right
            if n2 == Dir.left:
                return Dir.left

        if n1 == Dir.right:
            if n2 == Dir.down:
                return Dir.right
            if n2 == Dir.up:
                return Dir.left

        if n1 == Dir.down:
            if n2 == Dir.left:
                return Dir.right
            if n2 == Dir.right:
                return Dir.left

        if n1 == Dir.left:
            if n2 == Dir.up:
                return Dir.right
            if n2 == Dir.down:
                return Dir.left
        return Dir.none

    def __str__(self) -> str:
        res = {
            Dir.up: "↑",
            Dir.right: "→",
            Dir.left: "←",
            Dir.down: "↓",
            Dir.none: "-"
        }

        return res[self]
