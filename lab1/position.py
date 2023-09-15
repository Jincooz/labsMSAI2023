from enum import Enum

class CardinalDirections(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

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
    
    def __hash__(self) -> int:
        return int(self.x * 1000000 + self.y).__hash__()