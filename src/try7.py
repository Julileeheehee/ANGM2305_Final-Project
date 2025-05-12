import pygame
from enum import Enum
import random
from typing import Self
import threading

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

tileWeights = {
    "WATER" : 3,
    "COAST" : 1,
    "GRASS" : 10
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
        #self.img = pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))
        self.rect = self.img.get_rect()
        #self.is_tile_changed = False
        #self.collapsed = self.is_collapsed()

    def set_available_tiles(self, north_neighbor: Self | None=None , east_neighbor: Self|None=None, south_neighbor:Self|None=None, west_neighbor:Self|None=None):
        for tile_type in TileType:
            self.available_tiles.add(tile_type)
        
        self.update_tiles_from_neighbor(north_neighbor)
        self.update_tiles_from_neighbor(east_neighbor)
        self.update_tiles_from_neighbor(south_neighbor)
        self.update_tiles_from_neighbor(west_neighbor)
    
    def update_tiles_from_neighbor(self, neighbor: Self|None):
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

    #def is_collapsed(self):
     #   if self.get_entropy() == 1:
      #      return True
       # else:
        #    return False
    
    def pick_tile(self):
        weight = [tileWeights[possibility.name] for possibility in self.available_tiles]
        #print(weight)
        #self.tile_type = random.choice(list(self.available_tiles))
        #print(self.tile_type)
        self.tile_type = random.choices(list(self.available_tiles), weights=weight)
        self.tile_type = self.tile_type[0]
        #self.tile_type = random.choice(list(self.available_tiles))
        #self.is_tile_changed = True
        self.img = pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

    def get_tile_image(self):
        return pygame.transform.scale(pygame.image.load(self.tile_type.value), (64, 64))

def print_grid(grid: list[list[Tile | None]], screen):
    #print_text = "Printing the grid:"
    #print(print_text)
    #print('-' * len(print_text))
    null_state = pygame.transform.scale(pygame.image.load('images/3-tiles/blank_tile.png'), (64, 64))


    ##### This is ugly and def hardcoded
    #y = 1
    for row in range(len(grid)):
        #x = 1
        for col in range(len(grid[0])):
            if grid[row][col].tile_type: # if it exists/not None
                screen.blit(grid[row][col].get_tile_image(), (row*64 + PADDING, col*64 + PADDING*2))
            else:
                screen.blit(null_state, (row*64 + PADDING, col*64 + PADDING*2))
            #x+=1
        #y+=1
        

def determine_next_neighbor_coordinates(grid: list[list[Tile | None]], row: int, col: int):
    list_of_next_coordinates: list[tuple[int, int]] = []
    #north
    if col - 1 >= 0 and grid[row][col - 1] and grid[row][col - 1].tile_type == None:
        #print(grid[row][col - 1].tile_type)
        list_of_next_coordinates.append((row, col - 1))
    #east
    if row + 1 < len(grid) and grid[row + 1][col] and grid[row + 1][col].tile_type == None:
        #print(grid[row + 1][col].tile_type)
        list_of_next_coordinates.append((row + 1, col))
    #south
    if col + 1 < len(grid[0]) and grid[row][col + 1] and grid[row][col + 1].tile_type == None:
        #print(grid[row][col + 1].tile_type)
        list_of_next_coordinates.append((row, col + 1))
    #west
    if row - 1 >= 0 and grid[row - 1][col] and grid[row - 1][col].tile_type == None:
        #print(grid[row - 1][col].tile_type)
        list_of_next_coordinates.append((row - 1, col))

    return list_of_next_coordinates

def get_tile_from_coordinates(grid : list[list[Tile|None]], row:int, col:int):
    # check if the grid at the coordinate is not out of bounds
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return None

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType, screen):
    #is_grid_collapsed = False
    #list_of_collapsed : list[tuple[int,int]] = []
    grid[starting_row][starting_col].tile_type = starting_tile

    #list_of_collapsed.append([starting_row, starting_col])

    next_neighbor_coordinates: list[tuple[int, int]] = determine_next_neighbor_coordinates(grid, starting_row, starting_col)

    while next_neighbor_coordinates:
        pygame.time.delay(50)
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

                if grid[row][col].tile_type ==None:
                    lowest_entropy = 3 # 3 is the highest entropy
                    if entropy < lowest_entropy: 
                        list_of_low_entropy_coordinates.clear()
                        list_of_low_entropy_coordinates.append(coordinate)
                        lowest_entropy = entropy
                    elif entropy == lowest_entropy:
                        list_of_low_entropy_coordinates.append(coordinate)

                        

        
        if list_of_low_entropy_coordinates:
            print("not done")
            coordinate_to_move_to = random.choice(list_of_low_entropy_coordinates)
            next_neighbor_coordinates.remove(coordinate_to_move_to)

            move_to_row, move_to_col = coordinate_to_move_to
            #list_of_collapsed.append([move_to_row, move_to_col])
            grid[move_to_row][move_to_col].pick_tile()
            #print_grid(grid, screen)
            next_neighbor_coordinates.extend(determine_next_neighbor_coordinates(grid, move_to_row, move_to_col))
        else:
            print("done")
            return

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



def draw_grid_lines(screen : pygame.Surface):
    for col in range(NUM_OF_ROWS_COLS + 1):
        x = (col * PIXEL_DIM_OF_TILE) + PADDING
        pygame.draw.line(screen, WHITE, (x,PADDING*2), (x, 640 + PADDING*2), width=1)
    
    for row in range(NUM_OF_ROWS_COLS + 1):
        y = (row * PIXEL_DIM_OF_TILE) + PADDING * 2
        pygame.draw.line(screen, WHITE, (PADDING, y), (640 + PADDING, y), width=1)
    #tile_size = GRID_WIDTH//3
    #for row in range(0, GRID_WIDTH - 1, tile_size):
     #   for col in range(0, GRID_HEIGHT - 1, tile_size):
      #      rect = pygame.Rect(row, col, tile_size, tile_size)
       #     pygame.draw.rect(screen, BLACK, rect, 2)

class Button:
    def __init__(self, x:int, y:int, image: str):
        self.img = pygame.transform.scale(pygame.image.load(image), (64, 64))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    
    def get_rectangle(self):
        return self.rect
    
    def start_loop(self, grid: list[list[Tile | None]], starting_row:int, starting_col:int, starting_tile:TileType, screen:pygame.Surface):
        thread = threading.Thread(target=fill_grid, args=(grid, starting_row, starting_col, starting_tile, screen))
        thread.start()
        





        










def main():
    #num_of_rows = int(input("How many rows would you like?: "))
    #num_of_cols = int(input("How many columns would you like?: "))
    grid: list[list[Tile | None]] = [[Tile() for col in range(10)] for row in range(10)]
    #print_grid(grid)

    starting_row = 2
    starting_col = 2
    #outline = pygame.draw.rect(screen, WHITE, (starting_row, starting_col, 64, 64), width = 2)
    starting_tile = TileType.WATER

    


    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    fps = 24
    start_button = Button(800, 400, "images/3-tiles/blank_tile.png")
    reset_button = Button(900, 400, "images/3-tiles/blank_tile.png")
    water_button = Button(900, 200, "images/3-tiles/water_tile.png")
    coast_button = Button(975, 200, "images/3-tiles/coastline_tile.png")
    grass_button = Button(1050, 200, "images/3-tiles/grass_tile.png")
    



    
    #fill_grid(grid, 2, 2, TileType.WATER, screen)
    #print_grid(grid, screen)


    panels = Panels()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.get_rectangle().collidepoint(event.pos):
                    print("click")
                    start_button.start_loop(grid, starting_row, starting_col, starting_tile, screen)
                if reset_button.get_rectangle().collidepoint(event.pos):
                    print("reset")
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
                #clicked = False
                #pos = pygame.mouse.get_pos()
                #if button.get_rectangle().collidepoint(pos): # hovering over
                 #   if pygame.mouse.get_pressed()[0] and not clicked: # left mouse click. Middle is 1, and 2 is right
                  #      clicked = True
                   #     print("clicked")
                    #    fill_grid(grid, 2, 2, TileType.WATER, screen)
                    #if not pygame.mouse.get_pressed()[0]:
                     #   clicked = False


        #backgrounds
        screen.fill(GRAY)
        panels.update()

        #draw
        #draw_grid(screen)
        #pygame.draw.rect(screen, WHITE, (starting_row + PADDING*2, starting_col + PADDING, 64, 64), width = 5)
        print_grid(grid, screen)
        draw_grid_lines(screen)
        #fill_grid(grid, 2, 2, TileType.WATER, screen)
        start_button.draw(screen)
        reset_button.draw(screen)
        water_button.draw(screen)
        coast_button.draw(screen)
        grass_button.draw(screen)
        #pygame.draw.rect(screen, WHITE, (starting_row*PIXEL_DIM_OF_TILE + PADDING, starting_col*PIXEL_DIM_OF_TILE + PADDING*2, 64, 64), width = 5)
        if starting_tile == TileType.WATER:
            pygame.draw.rect(screen, BLACK, (900, 200, 64, 64), width = 5)
        elif starting_tile == TileType.COAST:
            pygame.draw.rect(screen, BLACK, (975, 200, 64, 64), width = 5)
        elif starting_tile == TileType.GRASS:
            pygame.draw.rect(screen, BLACK, (1050, 200, 64, 64), width = 5)
        pygame.draw.rect(screen, WHITE, (starting_row*PIXEL_DIM_OF_TILE + PADDING, starting_col*PIXEL_DIM_OF_TILE + PADDING*2, 64, 64), width = 5) #I'm not sure how this is working and why it's backward


        #get mouse pos and convert it to grid size
        pos = pygame.mouse.get_pos()
        x = (pos[1] - PADDING*2)//PIXEL_DIM_OF_TILE
        y = (pos[0] - PADDING)//PIXEL_DIM_OF_TILE
        

        #print([x,y])
        
        if pos[0] < 640+PADDING and pos[1] < 640+ PADDING*2: # Keeps it within the space
            if pygame.mouse.get_pressed()[0]==1:
                starting_col = x
                starting_row = y
        


        


        #flip display
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()