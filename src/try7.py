import pygame
from enum import Enum
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (77, 77, 77)

class TileType(Enum):
    COAST = 'C'
    GRASS = 'G'


class Tile:
    def __init__(self):
        self.tile_type : TileType | None = None
        self.available_tiles: set[TileType] = set()

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



def print_grid(grid: list[list[Tile | None]]):
    print_text = "Printing the grid:"
    print(print_text)
    print('-' * len(print_text))

    for col in grid:
        for row in col:
            if row.tile_type: # if it exists/not None
                print(row.tile_type.value, end=" ")
            else:
                print("-", end=" ")
        print()
    print()

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

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType):
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

def main():
    #num_of_rows = int(input("How many rows would you like?: "))
    #num_of_cols = int(input("How many columns would you like?: "))
    #grid: list[list[Tile | None]] = [[Tile() for col in range(num_of_cols)] for row in range(num_of_rows)]
    #print_grid(grid)

    #starting_row = int(input(f"Row? (0-{num_of_rows}): "))
    #starting_col = int(input(f"Col? (0-{num_of_cols}): "))
    #starting_tile = TileType(input("Tile? (W, C, G): "))

    #fill_grid(grid, starting_row, starting_col, starting_tile)
    #print_grid(grid)
    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #backgrounds
        screen.fill(GRAY)




        #flip display
        pygame.display.flip()
        clock.tick()

    pygame.quit()

if __name__ == "__main__":
    main()