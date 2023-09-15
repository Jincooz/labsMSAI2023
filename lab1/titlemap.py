import pygame

from map import Map
from agent import Agent

# dimension of each tiles
TILE_SIZE = 32

# texture of colors
YELLOW  = (255, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0 , 0, 255)
YEGREN  = (127, 255, 0)
GREEN   = (0, 255, 0)
BROWN   = (160, 82, 45)
WHITE   = (255,255,255)
BLACK   = (0,0,0)

def create_square_texture(color):
    image = pygame.Surface((TILE_SIZE, TILE_SIZE))
    image.fill(color)
    return image

def drow_circle_on_texture(image, color):
    pygame.draw.circle(image, color = color, center=(TILE_SIZE/2, TILE_SIZE/2), radius=TILE_SIZE/4)

# 0x0 -> grass
# 0xb -> dirt
textures = {
    "red_square" : create_square_texture(RED),
    "blue_square" : create_square_texture(BLUE),
    "white_square" : create_square_texture(WHITE),
    "black_square" : create_square_texture(BLACK)
}

# generate with tiles randomly
def generate_map(map : Map, tilesize = TILE_SIZE):
    map_data = []
    for i in range(map.map_height + 1):
        map_data.append([])
        for j in range(map.map_width + 1):
            map_data[i].append("white_square")
        map_data[i][-1] = "black_square"
    for j in range(map.map_width + 1):
        map_data[-1][j] = ("black_square")
    for position in map.get_exit_poitions():
        map_data[position.y][position.x] = "blue_square"
    for position in map.get_treasure_positions():
        map_data[position.y][position.x] = "red_square"
    return map_data

def draw_map(screen, map : Map, agent : Agent, history_of_agents_positions : set()):
    map_data = generate_map(map, agent)
    MAP_HEIGHT = len(map_data) 
    MAP_WIDTH = len(map_data[0])
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            image_to_draw = textures[map_data[row][col]].copy()
            for position in history_of_agents_positions:
                if(position.x == col and position.y == row):
                    drow_circle_on_texture(image_to_draw, YELLOW)
            for position in agent.position_visited:
                if(position.x == col and position.y == row):
                    drow_circle_on_texture(image_to_draw, GREEN)
            if col == agent.map_position.x and row == agent.map_position.y:
                drow_circle_on_texture(image_to_draw, BROWN)
            screen.blit(image_to_draw,
                        (col*TILE_SIZE, row*TILE_SIZE))