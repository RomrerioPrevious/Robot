from models import Dir, Node
from logger import *


class MainHandler:
    def __init__(self):
        ...

    def find_route(self, map: Node, start_name: str) -> [Dir]:
        self.calculate_dirs(map, start_name)

        result = []
        node = map.get_node("13")
        while start_name != node.name:
            result.append(node.dir)
            node = node.get_next_node_by_dir()

        return result

    def calculate_dirs(self, map: Node, start_name: str) -> None:
        start: Node = map.get_node(start_name)
        next = start.get_neighbors()
        next_starts = [start]
        while len(next) != 0:
            for prev in next_starts:
                if prev is None:
                    continue
                for i in next:
                    if i is None:
                        continue
                    if i.get_relative_position(prev) == Dir.none:
                        continue
                    if i.min == 0 or self.get_new_path_len(prev, i) < i.min:
                        i.dir = i.get_relative_position(prev)
                        i.min = self.get_new_path_len(prev, i)
                        self.check(i)
            next_starts = next
            next = []
            for i in next_starts:
                if i is None:
                    continue
                neighbors = i.get_neighbors()
                for n in neighbors:
                    if n is None or n.min != 0:
                        continue
                    if n not in next:
                        next.append(n)
            if start in next:
                next.remove(start)

    def check(self, node: Node):
       neighbors = node.get_neighbors()
       for i in neighbors:
           if i is None or node.dir == node.get_relative_position(i):
               continue
           if self.get_new_path_len(node, i) < i.min:
               i.dir = i.get_relative_position(node)
               i.min = self.get_new_path_len(node, i)
               self.check(i)



    def get_new_path_len(self, prev: Node, node: Node) -> int:
        return prev.min + node.get_len_by_dir(node.get_relative_position(prev))

