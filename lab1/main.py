from enum import Enum
import simpleai
import time

from map import *
import mapFileReaderWriter
from agent import Agent

from simpleai.search import SearchProblem, astar, breadth_first

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
    
    def __str__(self) -> str:
        return str(self.agent.map_position)

class MapTreasureProblem(SearchProblem):
    def actions(self, state):
        if(state.is_exit()):
            return []
        return state.posible_actions()

    def result(self, state, action):
        return state.move(action)

    def is_goal(self, state):
        return state.is_final()

class StateMachine:
    def __init__(self, state : State, screen) -> None:
        self.state = state
        time.sleep(1)
        self.screen.fill((255,255,255))
        draw_map(self.screen, state.map, state.agent, history_of_agents_positions)
        pygame.display.flip()

    def DFS(self, limit = -1):
        #TODO: Rewrite this method to look like BFS but based on stack
        def DFS_2(self, stack, limit):
            if(stack[-1].is_final()):
                return stack[-1].agent
            elif (stack[-1].is_exit()):
                return None
            if(limit == 0):
                return None
            for diraction in stack[-1].posible_actions():
                stack.append(stack[-1].move(diraction))
                self.refresh_screen(stack[-1])
                result = DFS_2(self, stack, limit - 1)
                if(result is not None):
                    return result
                stack.pop()
                self.refresh_screen(stack[-1])
        stack = list()
        stack.append(self.state)
        return DFS_2(self, stack, limit)
                
    def BFS(self, limit = -1):
        quene = list()
        quene.append(self.state)
        while len(quene) != 0:
            current_state = quene.pop(0)
            self.refresh_screen(current_state)
            if current_state.is_final():
                return current_state.agent
            elif current_state.is_exit():
                continue
            if(len(current_state.agent.position_visited) == limit + 1):
                continue
            for direction in current_state.posible_actions():
                next_state = current_state.move(direction)
                quene.append(next_state)
        return None

def get_example_map():
    return Map(5,5, [Position(0,1),Position(1,1),Position(2,2), Position(2,4), Position(4,1)], [Position(2,1),Position(4,2)])
    
def get_example_map2():
    return Map(5,5, [Position(0,1),Position(1,1),Position(2,2), Position(2,4), Position(4,1),Position(2,1)], [Position(0,0)])

def main():
    map = get_example_map()
    agent = Agent(Position(0,3))
    state = State(agent, map)
    problem = MapTreasureProblem(initial_state = state)
    result = breadth_first(problem)

    print(result.state)
    for element in result.path():
        print("("+str(element[0])+"), "+str(element[1])) 

if (__name__ == '__main__'):
    main()