from enum import Enum

class DoorColor(Enum):
    RED = 1 #door to exit
    GREEN = 2 #treasure nrae this room
    BLUE = 3 #nothing special

class CardinalDirections(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, 1)
    DOWN = (0, -1)

class Position:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __add__(self, other : CardinalDirections):
        return Position(self.x + other.value[0], self.y + other.value[1])
    
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"    

class Map:
    def __init__(self, map_width, map_height, exit_positions, treasure_positions) -> None:
        self.map_width = map_width
        self.map_height = map_height
        self.exit_positions = exit_positions
        self.treasure_positions = treasure_positions
        #calc empty positions
        #TODO: fix O(self.map_width * self.map_height * (len(exit_positions) + len(treasure_positions))) complexity
        self.empty_positions = []
        for x in range(self.map_width):
            for y in range(self.map_height):
                curent_position_is_empty = True
                for exit_position in exit_positions:
                    if(exit_position.x == x and exit_position.y == y):
                        curent_position_is_empty = False
                        break
                for treasure_position in treasure_positions:
                    if(treasure_position.x == x and treasure_position.y == y):
                        curent_position_is_empty = False
                        break
                if(curent_position_is_empty):
                    self.empty_positions.append(Position(x,y))
        
        self.door_map = [[DoorColor.BLUE for x in range(self.map_width)] for y in range(self.map_height)]
        for treasure_poition in self.treasure_positions:
            for x in range(max(treasure_poition.x - 1, 0), min(treasure_poition.x + 1, map_width)):
                for y in range(max(treasure_poition.y - 1, 0), min(treasure_poition.y + 1, map_height)):
                    self.door_map[x][y] = DoorColor.GREEN
            self.door_map[treasure_poition.x][treasure_poition.y] = DoorColor.GREEN
        for exit_position in self.exit_positions:
            self.door_map[exit_position.x][exit_position.y] = DoorColor.BLUE

    def get_treasure_positions(self):
        return self.treasure_positions

    def is_treasure_position(self, position):
        return position in self.treasure_positions

    def get_exit_poitions(self):
        return self.exit_positions
    
    def get_empty_positions(self):
        return self.empty_positions
    
    def get_door_color(self, from_position : Position, to_position : Position):
        return self.door_map[to_position.x][to_position.y]

    def get_posible_actions(self, agent_position) -> list(CardinalDirections):
        posible_moves = []
        if(agent_position.x != 0):
            posible_moves.append(CardinalDirections.LEFT)
        if(agent_position.x != self.map_width - 1):
            posible_moves.append(CardinalDirections.RIGHT)
        if(agent_position.y != self.map_height - 1):
            posible_moves.append(CardinalDirections.UP)
        if(agent_position.y != 0):
            posible_moves.append(CardinalDirections.DOWN)
        return posible_moves

class MapFileReaderWriter:
    def read_map(self, file_path) -> Map:
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
    
    def write_map(self, file_path, map : Map) -> None:
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

class Agent:
    def __init__(self, agent_position : Position) -> None:
        self.map_position = agent_position
    
    def get_position(self):
        return self.map_position

class State:
    def __init__(self, agent : Agent, map : Map) -> None:
        self.agent = agent
        self.map = map

    def posible_actions(self):
        return self.map.get_posible_actions(self.agent.map_position)
    
    def is_final(self):
        return self.map.is_treasure_position(self.agent.map_position)

    def move(self, action : CardinalDirections):
        self.agent.map_position += action

def get_example_map():
    return Map(5,5, [Position(0,3),Position(1,3),Position(2,2), Position(2,0), Position(4,3)], [Position(2,3),Position(4,2)])
    
def main():
    #TODO: Visualizer
    map = MapFileReaderWriter().read_map("example.map")

    pass

if (__name__ == '__main__'):
    main()