from enum import Enum
import pygame
import time

from map import *
import mapFileReaderWriter
from titlemap import draw_map
from agent import Agent

history_of_agents_positions = set()
class State:
    def __init__(self, agent : Agent, map : Map) -> None:
        self.agent = agent
        self.map = map
        history_of_agents_positions.add(self.agent.get_position())

    def posible_actions(self):
        return self.map.get_posible_actions(self.agent.map_position)
    
    def is_final(self):
        return self.map.is_treasure_position(self.agent.map_position)

    def is_exit(self):
        return self.map.is_exit_position(self.agent.map_position)

    def move(self, action : CardinalDirections):
        new_agent_position = self.agent.map_position + action
        new_agent = Agent(new_agent_position, self.agent.position_visited.copy())
        return State(new_agent, self.map)
    
    def copy(self):
        return State(self.agent, self.map)
    
def get_example_map():
    return Map(5,5, [Position(0,1),Position(1,1),Position(2,2), Position(2,4), Position(4,1)], [Position(2,1),Position(4,2)])
    
def get_example_map2():
    return Map(5,5, [Position(0,1),Position(1,1),Position(2,2), Position(2,4), Position(4,1),Position(2,1)], [Position(0,0)])
def main():
    map = mapFileReaderWriter.read_map("lab1/example.map")
    agent = Agent(Position(0,3))
    state = State(agent, map)
    screen = pygame.display.set_mode((640, 480))
    screen.fill((255,255,255))
    draw_map(screen, map, agent, history_of_agents_positions)
    pygame.display.flip()
    pass

if (__name__ == '__main__'):
    pygame.init()
    main()
pygame.quit()