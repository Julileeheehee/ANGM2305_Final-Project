import pygame
from enum import Enum
import random

SCREEN_WIDTH = 1280 # weird numbers I know
SCREEN_HEIGHT = 840 # TODO: Maybe calculate to be 720?

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (77, 77, 77)

# grid/panel sizes

# TODO: Make these numbers adjustable
GRID_WIDTH = 640
GRID_HEIGHT = 640

PANEL_WIDTH = 490
PANEL_HEIGHT = 640

PADDING = 50

# Columns and Rows for the grid
#TODO: Make these numbers adjustable later
NUM_OF_ROWS_COLS = 10

PIXEL_DIM_OF_TILE = 64
SCALE = (640/NUM_OF_ROWS_COLS)/PIXEL_DIM_OF_TILE





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
        #self.img = pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))
        self.rect = self.img.get_rect()
        self.is_tile_changed = False

    def set_available_tiles(self, north_neighbor, east_neighbor, south_neighbor, west_neighbor):
        for tile_type in TileType:
            self.available_tiles.add(tile_type)
        
        self.update_tiles_from_neighbor(north_neighbor)
        self.update_tiles_from_neighbor(east_neighbor)
        self.update_tiles_from_neighbor(south_neighbor)
        self.update_tiles_from_neighbor(west_neighbor)
    
    def update_tiles_from_neighbor(self, neighbor):
        #checks if these exist and are not None
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
        self.tile_type = random.choice(list(self.available_tiles))
        self.is_tile_changed = True
        self.img = pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

    def get_tile_image(self):

        return pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

def print_grid(grid: list[list[Tile | None]], screen):
    #print_text = "Printing the grid:"
    #print(print_text)
    #print('-' * len(print_text))
    null_state = pygame.transform.scale(pygame.image.load('images/3-tiles/blank_tile.png'), (64, 64))


    ##### This is ugly and def hardcoded
    y = 1
    for row in grid:
        x = 1
        for col in row:
            if col.tile_type: # if it exists/not None
                screen.blit(col.get_tile_image(), (x*64, y*64))
            else:
                screen.blit(null_state, (x*64, y*64))
            x+=1
        y+=1
        

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

def get_tile_from_coordinates(grid, row, col):
    # check if the grid at the coordinate is not out of bounds
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return None

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType, screen):
    #is_grid_collapsed = False
    grid[starting_row][starting_col].tile_type = starting_tile

    next_neighbor_coordinates: list[tuple[int, int]] = determine_next_neighbor_coordinates(grid, starting_row, starting_col)

    while next_neighbor_coordinates:
        list_of_low_entropy_coordinates: list[tuple[int,int]] = []

        for coordinate in next_neighbor_coordinates: # coordinate should be a tuple(x,y)
            row, col = coordinate
            tile: Tile | None = get_tile_from_coordinates(grid, row, col)
            
            if tile != None:
                north_neighbor = get_tile_from_coordinates(grid, row, col - 1)
                east_neighbor = get_tile_from_coordinates(grid, row + 1, col)
                south_neighbor = get_tile_from_coordinates(grid, row, col + 1)
                west_neighbor = get_tile_from_coordinates(grid, row - 1, col)

                tile.set_available_tiles(north_neighbor, east_neighbor, south_neighbor, west_neighbor)

                entropy = tile.get_entropy()

                lowest_entropy = 3 # 3 is the highest entropy
                if entropy < lowest_entropy: 
                    list_of_low_entropy_coordinates.clear()
                    list_of_low_entropy_coordinates.append(coordinate)
                    lowest_entropy = entropy
                elif entropy == lowest_entropy:
                    list_of_low_entropy_coordinates.append(coordinate)
        
        coordinate_to_move_to = random.choice(list_of_low_entropy_coordinates)
        next_neighbor_coordinates.remove(coordinate_to_move_to)

        move_to_row, move_to_col = coordinate_to_move_to
        grid[move_to_row][move_to_col].pick_tile()
        next_neighbor_coordinates.extend(determine_next_neighbor_coordinates(grid, move_to_row, move_to_col))

class Panels:
    def __init__(self):
        self.surface_left = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        pygame.Surface.fill(self.surface_left, WHITE)

        self.surface_right = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
        pygame.Surface.fill(self.surface_right, WHITE)

        self.display_surface = pygame.display.get_surface()

    def update(self):
        self.display_surface.blit(self.surface_left, (PADDING, PADDING*2)) # Purple in picture
        self.display_surface.blit(self.surface_right, (PADDING*2 + GRID_WIDTH, PADDING*2)) # light blue in picture



def draw_grid(screen):
    tile_size = GRID_WIDTH//3
    for row in range(0, GRID_WIDTH - 1, tile_size):
        for col in range(0, GRID_HEIGHT - 1, tile_size):
            rect = pygame.Rect(row, col, tile_size, tile_size)
            pygame.draw.rect(screen, BLACK, rect, 2)

class Button:
    def __init__(self, x, y):
        self.img = pygame.transform.scale(pygame.image.load("images/3-tiles/blank_tile.png"), (64*0.99, 64*0.99))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    
    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): # hovering over
            if pygame.mouse.get_pressed()[0] and not self.clicked: # left mouse click. Middle is 1, and 2 is right
                self.clicked = True
                print("clicked")
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        screen.blit(self.img, (self.rect.x, self.rect.y))





        










def main():
    #num_of_rows = int(input("How many rows would you like?: "))
    #num_of_cols = int(input("How many columns would you like?: "))
    grid: list[list[Tile | None]] = [[Tile() for col in range(10)] for row in range(10)]
    #print_grid(grid)

    #starting_row = int(input(f"Row? (0-{num_of_rows}): "))
    #starting_col = int(input(f"Col? (0-{num_of_cols}): "))
    #starting_tile = TileType(input("Tile? (W, C, G): "))

    


    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    fps = 24

    #fill_grid(grid, 2, 2, TileType.WATER)
    #print_grid(grid, screen)


    panels = Panels()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            

        #backgrounds
        screen.fill(GRAY)
        panels.update()

        #draw
        #draw_grid(screen)
        print_grid(grid, screen)
        fill_grid(grid, 2, 2, TileType.WATER, screen)
        


        #flip display
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()