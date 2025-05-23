# Imports-----------------------------------------------------------
# 3rd party
import pygame
import pygame_widgets #python -m pip install pygame-widgets
from pygame_widgets.slider import Slider

# Built-in
from enum import Enum
import random
from typing import Self
import threading


# Constants----------------------------------------------------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 840 # TODO: Maybe calculate to be 720?

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (77, 77, 77)

# TODO: Make these numbers adjustable in the future
GRID_WIDTH = 640
GRID_HEIGHT = 640
PANEL_WIDTH = 490
PANEL_HEIGHT = 640
PADDING = 50

#TODO: Make these numbers adjustable later
NUM_OF_ROWS_COLS = 10
PIXEL_DIM_OF_TILE = 64

# Water and Grass are equally chosen, but these values can change to produce a higher likelihood of picking a specific tile
tileWeights = {
    "WATER" : 0.5,
    "COAST" : 0.1,
    "GRASS" : 0.5
}

class TileType(Enum):
    WATER = 'images/3-tiles/water_tile.png'
    COAST = 'images/3-tiles/coastline_tile.png'
    GRASS = 'images/3-tiles/grass_tile.png'

class Tile:
    def __init__(self):
        self.null_state = pygame.transform.scale(pygame.image.load('images/3-tiles/blank_tile.png'), (64, 64))
        self.tile_type : TileType | None = None
        self.available_tiles: set[TileType] = set()
        self.img = self.null_state

    def set_available_tiles(self, north_neighbor: Self | None=None , east_neighbor: Self|None=None, south_neighbor:Self|None=None, west_neighbor:Self|None=None):
        for tile_type in TileType:
            self.available_tiles.add(tile_type)
        
        self.update_tiles_from_neighbor(north_neighbor)
        self.update_tiles_from_neighbor(east_neighbor)
        self.update_tiles_from_neighbor(south_neighbor)
        self.update_tiles_from_neighbor(west_neighbor)
    
    def update_tiles_from_neighbor(self, neighbor: Self|None):
        if neighbor and neighbor.tile_type: 
            if neighbor.tile_type == TileType.WATER:
                self.available_tiles &= set([TileType.WATER, TileType.COAST])
            elif neighbor.tile_type == TileType.COAST:
                self.available_tiles &= set([TileType.WATER, TileType.COAST, TileType.GRASS])
            elif neighbor.tile_type == TileType.GRASS:
                self.available_tiles &= set([TileType.COAST, TileType.GRASS])
    
    def get_entropy(self):
        return len(self.available_tiles)
    
    def pick_tile(self):
        weight = [tileWeights[possibility.name] for possibility in self.available_tiles]
        self.tile_type = random.choices(list(self.available_tiles), weights=weight)
        self.tile_type = self.tile_type[0]
        self.img = pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

    def get_tile_image(self):
        return pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

def print_grid(grid: list[list[Tile | None]], screen):
    null_state = pygame.transform.scale(pygame.image.load('images/3-tiles/blank_tile.png'), (64, 64))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].tile_type:
                screen.blit(grid[row][col].get_tile_image(), (row*64 + PADDING, col*64 + PADDING*2))
            else:
                screen.blit(null_state, (row*64 + PADDING, col*64 + PADDING*2))
  
def determine_next_neighbor_coordinates(grid: list[list[Tile | None]], row: int, col: int):
    list_of_next_coordinates: list[tuple[int, int]] = []
    #north
    if col - 1 >= 0 and grid[row][col - 1] and grid[row][col - 1].tile_type == None:
        list_of_next_coordinates.append((row, col - 1))
    #east
    if row + 1 < len(grid) and grid[row + 1][col] and grid[row + 1][col].tile_type == None:
        list_of_next_coordinates.append((row + 1, col))
    #south
    if col + 1 < len(grid[0]) and grid[row][col + 1] and grid[row][col + 1].tile_type == None:
        list_of_next_coordinates.append((row, col + 1))
    #west
    if row - 1 >= 0 and grid[row - 1][col] and grid[row - 1][col].tile_type == None:
        list_of_next_coordinates.append((row - 1, col))

    return list_of_next_coordinates

def get_tile_from_coordinates(grid : list[list[Tile|None]], row:int, col:int):
    # check if the grid at the coordinate is not out of bounds
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return None

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType, speed: int):
    grid[starting_row][starting_col].tile_type = starting_tile
    next_neighbor_coordinates: list[tuple[int, int]] = determine_next_neighbor_coordinates(grid, starting_row, starting_col)

    while next_neighbor_coordinates:
        if speed != 0:
            pygame.time.delay(speed)
        list_of_low_entropy_coordinates: list[tuple[int,int]] = []

        for coordinate in next_neighbor_coordinates:
            row, col = coordinate
            tile: Tile | None = get_tile_from_coordinates(grid, row, col)
                
            if tile != None:
                north_neighbor = get_tile_from_coordinates(grid, row, col - 1)
                east_neighbor = get_tile_from_coordinates(grid, row + 1, col)
                south_neighbor = get_tile_from_coordinates(grid, row, col + 1)
                west_neighbor = get_tile_from_coordinates(grid, row - 1, col)
                tile.set_available_tiles(north_neighbor, east_neighbor, south_neighbor, west_neighbor)
            
                entropy = tile.get_entropy()

                if grid[row][col].tile_type ==None:
                    lowest_entropy = 3 # 3 is the highest entropy
                    if entropy < lowest_entropy: 
                        list_of_low_entropy_coordinates.clear()
                        list_of_low_entropy_coordinates.append(coordinate)
                        lowest_entropy = entropy
                    elif entropy == lowest_entropy:
                        list_of_low_entropy_coordinates.append(coordinate)
        
        if list_of_low_entropy_coordinates:
            coordinate_to_move_to = random.choice(list_of_low_entropy_coordinates)
            next_neighbor_coordinates.remove(coordinate_to_move_to)
            move_to_row, move_to_col = coordinate_to_move_to
            grid[move_to_row][move_to_col].pick_tile()
            next_neighbor_coordinates.extend(determine_next_neighbor_coordinates(grid, move_to_row, move_to_col))
        else:
            return

class Panels:
    def __init__(self):
        self.surface_left = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        pygame.Surface.fill(self.surface_left, WHITE)

        self.surface_right = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
        pygame.Surface.fill(self.surface_right, WHITE)

        self.display_surface = pygame.display.get_surface()

    def draw(self):
        self.display_surface.blit(self.surface_left, (PADDING, PADDING*2))
        self.display_surface.blit(self.surface_right, (PADDING*2 + GRID_WIDTH, PADDING*2))

def draw_grid_lines(screen : pygame.Surface):
    for col in range(NUM_OF_ROWS_COLS + 1):
        x = (col * PIXEL_DIM_OF_TILE) + PADDING
        pygame.draw.line(screen, WHITE, (x,PADDING*2), (x, 640 + PADDING*2), width=1)
    
    for row in range(NUM_OF_ROWS_COLS + 1):
        y = (row * PIXEL_DIM_OF_TILE) + PADDING * 2
        pygame.draw.line(screen, WHITE, (PADDING, y), (640 + PADDING, y), width=1)

class Button:
    def __init__(self, x:int, y:int, image: str):
        self.img = (pygame.image.load(image))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    
    def get_rectangle(self):
        return self.rect
    
    def start_loop(self, grid: list[list[Tile | None]], starting_row:int, starting_col:int, starting_tile:TileType, speed: int):
        thread = threading.Thread(target=fill_grid, args=(grid, starting_row, starting_col, starting_tile, speed))
        thread.start()

def set_speed(slider_value: int) -> int:
    updated_value = (-1*slider_value) + 200
    return updated_value

def draw_text(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    text_rect = img.get_rect(center=(x, y))
    screen.blit(img, text_rect)

def main():
    pygame.init()
    pygame.font.init()

    # pygame info
    label_font = pygame.font.Font("Juliette_handwritting-Regular.ttf", 45)
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    fps = 24

    # Algorithm info
    grid: list[list[Tile | None]] = [[Tile() for col in range(10)] for row in range(10)]
    starting_row = 2
    starting_col = 2
    starting_tile = TileType.WATER
    speed = 100
    
    # UI elements
    solve_button = Button(921, 530, "images/3-tiles/solve_button.png")
    reset_button = Button(921, 626, "images/3-tiles/reset_button.png")
    water_button = Button(847, 242, "images/3-tiles/water_tile.png")
    coast_button = Button(953, 242, "images/3-tiles/coastline_tile.png")
    grass_button = Button(1059, 242, "images/3-tiles/grass_tile.png")
    slider = Slider(screen, x=835, y=442, width=300, height=20, min=0, max=200, step=50)
    panels = Panels()
    
    running = True
    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.get_rectangle().collidepoint(event.pos):
                    solve_button.start_loop(grid, starting_row, starting_col, starting_tile, speed)
                if reset_button.get_rectangle().collidepoint(event.pos):
                    grid: list[list[Tile | None]] = [[Tile() for col in range(10)] for row in range(10)]
                if water_button.get_rectangle().collidepoint(event.pos):
                    starting_tile = TileType.WATER
                    pygame.draw.rect(screen, BLACK, (900, 200, 64, 64), width = 5)
                if coast_button.get_rectangle().collidepoint(event.pos):
                    starting_tile = TileType.COAST
                    pygame.draw.rect(screen, BLACK, (975, 200, 64, 64), width = 5)
                if grass_button.get_rectangle().collidepoint(event.pos):
                    starting_tile = TileType.GRASS
                    pygame.draw.rect(screen, BLACK, (1050, 200, 64, 64), width = 5)

        #backgrounds
        screen.fill(GRAY)
        panels.draw()

        # Left side
        print_grid(grid, screen)
        draw_grid_lines(screen)
        # Grid highlight
        pygame.draw.rect(screen, WHITE, (starting_row*PIXEL_DIM_OF_TILE + PADDING, starting_col*PIXEL_DIM_OF_TILE + PADDING*2, 64, 64), width = 5)

        # Right side
        solve_button.draw(screen)
        reset_button.draw(screen)
        water_button.draw(screen)
        coast_button.draw(screen)
        grass_button.draw(screen)
        draw_text(screen, "Pick first tile type", label_font, BLACK, 985, 185)
        draw_text(screen, "Speed", label_font, BLACK, 985, 385)
        draw_text(screen, "Pick first tile location", label_font, WHITE, 370, 60)
        # Button highlight
        if starting_tile == TileType.WATER:
            pygame.draw.rect(screen, BLACK, (847, 242, 64, 64), width = 5)
        elif starting_tile == TileType.COAST:
            pygame.draw.rect(screen, BLACK, (953, 242, 64, 64), width = 5)
        elif starting_tile == TileType.GRASS:
            pygame.draw.rect(screen, BLACK, (1059, 242, 64, 64), width = 5)
        
        # Updates
        pygame_widgets.update(pygame.event.get())
        speed = set_speed(slider.getValue())

        #get mouse pos and convert it to grid size
        pos = pygame.mouse.get_pos()
        x = (pos[1] - PADDING*2)//PIXEL_DIM_OF_TILE
        y = (pos[0] - PADDING)//PIXEL_DIM_OF_TILE
        # Keeps the mouse clicks within the left panel area
        if PADDING < pos[0] < 640+PADDING and PADDING*2 < pos[1] < 640+ PADDING*2: 
            if pygame.mouse.get_pressed()[0]==1:
                starting_col = x
                starting_row = y

        #flip display
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()