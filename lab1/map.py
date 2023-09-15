from enum import Enum

from position import CardinalDirections, Position

class DoorColor(Enum):
    RED = 1 #door to exit
    GREEN = 2 #treasure near this room
    BLUE = 3 #nothing special

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
    
    def is_exit_position(self, position):
        return position in self.exit_positions
    
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
            posible_moves.append(CardinalDirections.DOWN)
        if(agent_position.y != 0):
            posible_moves.append(CardinalDirections.UP)
        return posible_moves