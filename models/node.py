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

    min: int = 0

    up_dir: int = 1
    right_dir: int = 1
    down_dir: int = 1
    left_dir: int = 1

    dir: Dir = Dir.none

    def get_node(self, name: str) -> Any:
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

    def get_relative_position(self, node: Any) -> Dir:
        name = int(node.name)
        if self.name == str(name - 10):
            return Dir.right
        if self.name == str(name + 10):
            return Dir.left
        if self.name == str(name - 1):
            return Dir.down
        if self.name == str(name + 1):
            return Dir.up
        return Dir.none

    def get_next_node_by_dir(self) -> Any:
        if self.dir == Dir.left:
            return self.left
        if self.dir == Dir.right:
            return self.right
        if self.dir == Dir.up:
            return self.up
        if self.dir == Dir.down:
            return self.down


    def get_len_by_dir(self, dir: Dir):
        dirs = {
            Dir.up: self.up_dir,
            Dir.down: self.down_dir,
            Dir.left: self.left_dir,
            Dir.right: self.right_dir
        }
        return dirs[dir]

    def get_neighbors(self) -> []:
        return [self.left, self.right, self.up, self.down]

    @staticmethod
    def update_nodes_values(node, node_data):
        node.up_dir = node_data["u"]
        if node_data["u"] == 1:
            if node.up is not None:
                node.up_dir = node.up.down_dir
        else:
            if node.up is not None:
                node.up.down_dir = node_data["u"]
        node.down_dir = node_data["d"]
        if node_data["d"] == 1:
            if node.down is not None:
                node.down_dir = node.down.up_dir
        else:
            if node.down is not None:
                node.down.up_dir = node_data["d"]
        node.left_dir = node_data["l"]
        if node_data["l"] == 1:
            if node.left is not None:
                node.left_dir = node.left.right_dir
        else:
            if node.left is not None:
                node.left.right_dir = node_data["l"]
        node.right_dir = node_data["r"]
        if node_data["r"] == 1:
            if node.right is not None:
                node.right_dir = node.right.left_dir
        else:
            if node.right is not None:
                node.right.left_dir = node_data["r"]

    def __str__(self) -> str:
        return self.name

    def __hash__(self):
        return hash((self.name, self.min, self.dir))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (self.name, self.min, self.dir) == (other.name, other.min, other.dir)
