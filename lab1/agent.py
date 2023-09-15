from position import Position

class Agent:
    def __init__(self, agent_position : Position, position_visited = list()) -> None:
        self.map_position = agent_position
        self.position_visited = position_visited
        self.position_visited.append(agent_position)
    
    def get_position(self):
        return self.map_position