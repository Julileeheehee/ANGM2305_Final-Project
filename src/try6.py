from enum import Enum
# (done) Step 1: Initialize grid, cells, and all the tiles
# (done) Step 2: Pick the first spot and the tile to collapse to

# Step 3: Make a list of locations of collapsed cells (save as a tuple)
# Step 4: Grab the neighbors of collapsed cells, and remove tiles according to rules
# Step 5: Make a dictionary of entropy keys with location values of the neighbors (will be updated a lot)
# Step 6: Update entropy for grid via # tiles in cell
# Step 7: Pick a random location from the smallest key
# Step 8: If that cell has two tiles, pick a random tile
# Step 9: Collapse that cell and start back at step 3

# Step 10: If there are no options available (definitely possible), start over with with the inputs of step 2.
# Step 11: When the len(list of collapsed cells) == grid row x grid col, the map is complete


###### I basically learned that it's SUPER IMPORTANT to include the types of the parameters, so i'm doing my best to include it all the time#############



class TileType(Enum): # This handles the tile types without making a class. Enum is super useful for handling nonchangable stuff. This helps me reduce checking with if/else statements
    WATER = 'W'
    COAST = 'C'
    GRASS = 'G'

class Tile:
    def __init__(self):
        self.tile_type : TileType | None = None #Basically, the tile type is either a type or none. The default is none because it hasn't been collapsed yet

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

def determine_next_neighbor_coordinates(grid, row, col):
    # Take the grid, the location coordinates (x, y), and find the neighbors
    list_of_next_coordinates: list[tuple[int, int]] = []

    #determine north, east, south, west neighbors
    
    #north
    if col - 1 >= 0:
        list_of_next_coordinates.append((row, col - 1))
    #east
    if row + 1 < len(grid):
        list_of_next_coordinates.append((row + 1, col))
    #south
    if col + 1 < len(grid[0]):
        list_of_next_coordinates.append((row, col + 1))
    #west
    if row - 1 >= 0:
        list_of_next_coordinates.append((row - 1, col))

    return list_of_next_coordinates

def fill_grid(grid: list[list[Tile | None]], starting_row: int, starting_col: int, starting_tile: TileType):
    grid[starting_row][starting_col].tile_type = starting_tile

    next_neighbor_coordinates: list[tuple[int, int]] = determine_next_neighbor_coordinates(grid, starting_row, starting_col)
    print()
    print("Neighbor locations: ", end="")
    print(next_neighbor_coordinates)
    print()



def main():
    grid: list[list[Tile | None]] = [[Tile() for col in range(3)] for row in range(3)] # I learned that | means or, so I can make it a tile or none!
    print_grid(grid)

    starting_row = int(input("Row? (0-2): "))
    starting_col = int(input("Col? (0-2): "))
    starting_tile = TileType(input("Tile? (W, C, G): "))

    fill_grid(grid, starting_row, starting_col, starting_tile)
    print_grid(grid)

if __name__ == "__main__":
    main()