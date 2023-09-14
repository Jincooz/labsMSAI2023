

class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

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
    
    def get_posible_treasure_positions(self):
        return self.treasure_positions

    def get_exit_poitions(self):
        return self.exit_positions
    
    def get_empty_positions(self):
        return self.empty_positions

    def discover_position(self, position):
        pass

    def get_posible_actions(self, agent_position):
        posible_moves = []
        if(agent_position.x != 0):
            posible_moves.append("L")
        if(agent_position.x != self.map_width - 1):
            posible_moves.append("R")
        if(agent_position.y != self.map_height - 1):
            posible_moves.append("U")
        if(agent_position.y != 0):
            posible_moves.append("D")
        return posible_moves

class UndiscoveredMap(Map):
    def __init__(self, map_width, map_height, exit_positions, treasure_positions) -> None:
        Map.__init__(self, map_width, map_height, exit_positions, treasure_positions)
        self.discovered_exit_positions = []
        self.discovered_empty_positions = []
        self.discovered_posible_treasure_positions = []
        self.discovered_positions = []
    
    def get_posible_treasure_positions(self):
        return self.discovered_posible_treasure_positions

    def get_exit_poitions(self):
        return self.discovered_exit_positions
    
    def get_empty_positions(self) -> list(Position):
        return self.discovered_empty_positions

    def discover_position(self, agent_position) -> None:
        #TODO: write this method
        for discovered_position in self.discovered_positions:
            if(discovered_position.x == agent_position.x and discovered_position.y == agent_position.y):
                return
        self.discovered_positions.append(Position(agent_position.x,agent_position.y))
        x_range = range(max(0, agent_position.x - 2), min(agent_position.x + 2, self.map_width))
        y_range = range(max(0, agent_position.y - 2), min(agent_position.y + 2, self.map_height))
        nearby_map = [[]]
        for x in x_range:
            for y in y_range:
                pass


class State:
    def __init__(self, agent_position, map) -> None:
        self.agent_position = agent_position
        self.map = map

    def posible_actions(self):
        pass
    
    def is_final(self):
        pass

    def move(self, action):
        pass

def main():
    pass

if (__name__ == '__main__'):
    main()