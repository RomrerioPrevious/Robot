from handlers import MainHandler
from models import *
from handlers import *
from logger import *
import json


def create_map(path: str = r"resources/map.json") -> Node:
    result = Node("11")

    with open(path) as file:
        data = json.load(file)["map"]

    for symbol in range(7):
        for num in range(5):
            name = f"{symbol + 1}{num + 1}"
            node = Node(name)

            if name == "11":
                node = result

            left_node = result.get_node(str(int(name) - 10))
            up_node = result.get_node(str(int(name) - 1))

            if left_node is not None:
                left_node.right = node
            if up_node is not None:
                up_node.down = node

            node.left = left_node
            node.up = up_node

            if name not in data:
                node_data = {"u": 1, "l": 1, "r": 1, "d": 1}
            else:
                node_data = data[name]

            Node.update_nodes_values(node, node_data)

    return result


def main():
    log("Programm has been started")

    map = create_map()

    log("Map was been created")

    main_handler = MainHandler()
    robot_handler = RobotHandler()

    bar = robot_handler.read_barcode()
    coord = main_handler.read_barcode(bar)
    route = main_handler.find_route(map, coord)
    fin_dir = route[-1]

    robot_handler.follow_route(route)

    route = main_handler.back(coord, route[-1])
    robot_handler.follow_route(route, my_dir=fin_dir)
    if route == Dir.down:
        robot_handler.right()
    if route == Dir.up:
        robot_handler.left()

    color = coord[-1]
    rev = 0
    for i in range(len(bar)):
        if bar[-i] != color:
            rev += 1
            color = bar[-1]

    color = coord[-1]
    for i in range(rev):
        if color == "0":
            robot_handler.go_white()
            color = "1"
        elif color == "1":
            robot_handler.go_dark()
            color = "0"

    robot_handler.final()


if __name__ == "__main__":
    main()
