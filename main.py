from handlers import MainHandler, follow_route
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
                continue
            
            node_data = data[name]

            node.up_dir = node_data["u"]
            node.down_dir = node_data["d"]
            node.left_dir = node_data["l"]
            node.right_dir = node_data["r"]

    return result


def main():
    log("Programm has been started")

    map = create_map()

    log("Map was been created")

    main_handler = MainHandler()
    route = main_handler.find_route(map)

    follow_route(route)

    error("FUCK!!!")


if __name__ == "__main__":
    main()
