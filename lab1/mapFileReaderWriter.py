from map import Map, Position

def read_map(file_path) -> Map:
    try:
        file = open(file_path, "r")
        map_width = int(file.read(1))
        map_height = int(file.read(1))
        amount_of_exits = int(file.read(1))
        amount_of_treasures = int(file.read(1))
        exit_positions = []
        treasure_positions = []
        for _ in range(amount_of_exits):
            exit_x = int(file.read(1))
            exit_y = int(file.read(1))
            exit_positions.append(Position(exit_x, exit_y))
        for _ in range(amount_of_treasures):
            treasure_x = int(file.read(1))
            treasure_y = int(file.read(1))
            treasure_positions.append(Position(treasure_x, treasure_y))
        last = file.read()
        if last != '':
            raise Exception()
    except FileNotFoundError:
        raise Exception("File not found")
    except Exception:
        raise Exception("File corrupted")
    finally:
        file.close()
    return Map(map_width, map_height, exit_positions, treasure_positions)

def write_map(file_path, map : Map) -> None:
    with open(file_path, "w") as file:
        file.write(str(map.map_width))
        file.write(str(map.map_height))
        file.write(str(len(map.exit_positions)))
        file.write(str(len(map.treasure_positions)))
        for exit_position in map.exit_positions:
            file.write(str(exit_position.x))
            file.write(str(exit_position.y))
        for treasure_position in map.treasure_positions:
            file.write(str(treasure_position.x))
            file.write(str(treasure_position.y))