from enum import Enum
import random


###### I basically learned that it's SUPER IMPORTANT to include the types of the parameters, so i'm doing my best to include it all the time#############

# ANSI escape sequences:-----------------------------------
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'


RESET = '\033[0m' # called to return to standard terminal text color
#------------------------------------------------------------------

tileWeights = {
    "WATER" : 4,
    "COAST" : 1,
    "GRASS" : 10
}



class TileType(Enum): # This handles the tile types without making a class. Enum is super useful for handling nonchangable stuff. This helps me reduce checking with if/else statements
    WATER = 'W'
    COAST = 'C'
    GRASS = 'G'

class Tile:
    def __init__(self):
        self.tile_type : TileType | None = None #Basically, the tile type is either a type or none. The default is none because it hasn't been collapsed yet
        self.available_tiles: set[TileType] = set() # A set is basically a dictionary, but just the keys. Like a list, but cannot be indexed. A set is initialized with () but uses {}

    def set_available_tiles(self, north_neighbor, east_neighbor, south_neighbor, west_neighbor):
        #self.available_tiles: set[TileType] = set()
        for tile_type in TileType:
            self.available_tiles.add(tile_type) # no need to worry about duplicates
        
        self.update_tiles_from_neighbor(north_neighbor)
        self.update_tiles_from_neighbor(east_neighbor)
        self.update_tiles_from_neighbor(south_neighbor)
        self.update_tiles_from_neighbor(west_neighbor)
    
    def update_tiles_from_neighbor(self, neighbor):
        if neighbor and neighbor.tile_type: #checks if these exist and are not None
            if neighbor.tile_type == TileType.WATER:
                self.available_tiles &= set([TileType.WATER, TileType.COAST]) #learned a new assignment operator. Basically I'm combining two sets, the duplicates will be removed anyways because it's a set
            elif neighbor.tile_type == TileType.COAST:
                self.available_tiles &= set([TileType.WATER, TileType.COAST, TileType.GRASS])
            elif neighbor.tile_type == TileType.GRASS:
                self.available_tiles &= set([TileType.COAST, TileType.GRASS])


    def get_entropy(self):
        return len(self.available_tiles)
    
    def pick_tile(self):
        print(self.available_tiles)
        print(list(self.available_tiles))
        weight = [tileWeights[possibility.name] for possibility in self.available_tiles]
        #print(weight)
        #self.tile_type = random.choice(list(self.available_tiles))
        #print(self.tile_type)
        self.tile_type = random.choices(list(self.available_tiles), weights=weight)
        self.tile_type = self.tile_type[0]
        



def print_grid(grid: list[list[Tile | None]]):
    print_text = "Printing the grid:"
    print(print_text)
    print('-' * len(print_text))

    for col in grid:
        for row in col:
            if row.tile_type: # if it exists/not None
                print(row.tile_type.value, end=" ") #enum.value just returns the value, so row.WATER will return a value of W
            else:
                print("-", end=" ")
        print()
    print()

def determine_next_neighbor_coordinates(grid: list[list[Tile | None]], row: int, col: int):
    # Take the grid, the location coordinates (x, y), and find the neighbors
    list_of_next_coordinates: list[tuple[int, int]] = []

    #determine north, east, south, west neighbors
    #Must be None
    
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
    else: # OoB
        return None

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType):
    #is_grid_collapsed = False
    grid[starting_row][starting_col].tile_type = starting_tile

    next_neighbor_coordinates: list[tuple[int, int]] = determine_next_neighbor_coordinates(grid, starting_row, starting_col)

    #while the next_neighbor_coordinates has places to move to,
    #   loop through each location in the list
    #   grab the tile
    #   update the types it could be
    #   and calculate its entropy

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

                # From here: add the coordinates of the tiles with the lowest entropy
                lowest_entropy = 3 # 3 is the highest entropy
                if entropy < lowest_entropy: 
                    list_of_low_entropy_coordinates.clear() # removes the old coordinates that have higher entropy numbers
                    list_of_low_entropy_coordinates.append(coordinate)
                    lowest_entropy = entropy # Sets the lowest to the new entropy
                elif entropy == lowest_entropy: # basically we need to try to get this down to 1 or 2
                    list_of_low_entropy_coordinates.append(coordinate)
        
        # Pick a random coordinate fromm the list
        coordinate_to_move_to = random.choice(list_of_low_entropy_coordinates)
        # Remove that coordinate from next_neighbor_coordinates
        next_neighbor_coordinates.remove(coordinate_to_move_to)

        move_to_row, move_to_col = coordinate_to_move_to
        grid[move_to_row][move_to_col].pick_tile()

        next_neighbor_coordinates.extend(determine_next_neighbor_coordinates(grid, move_to_row, move_to_col))

def main():
    num_of_rows = int(input("How many rows would you like?: "))
    num_of_cols = int(input("How many columns would you like?: "))
    grid: list[list[Tile | None]] = [[Tile() for col in range(num_of_cols)] for row in range(num_of_rows)] # I learned that | means or, so I can make it a tile or none!
    print_grid(grid)

    starting_row = int(input(f"Row? (0-{num_of_rows - 1}): "))
    starting_col = int(input(f"Col? (0-{num_of_cols - 1}): "))
    starting_tile = TileType(input("Tile? (W, C, G): "))

    fill_grid(grid, starting_row, starting_col, starting_tile)
    print_grid(grid)

if __name__ == "__main__":
    main()