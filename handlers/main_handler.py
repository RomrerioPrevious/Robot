from models import Dir, Node


class MainHandler:
    def __init__(self):
        ...

    def find_route(self, map: Node) -> [Dir]:
        return [Dir.down]
