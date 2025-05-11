
# Step 1: Initialize grid, cells, and all the tiles
# Step 2: Pick the first spot and the tile to collapse to

# Step 3: Make a list of locations of collapsed cells (save as a tuple)
# Step 4: Grab the neighbors of collapsed cells, and remove tiles according to rules
# Step 5: Make a dictionary of entropy keys with location values of the neighbors (will be updated a lot)
# Step 6: Update entropy for grid via # tiles in cell
# Step 7: Pick a random location from the smallest key
# Step 8: If that cell has two tiles, pick a random tile
# Step 9: Collapse that cell and start back at step 3

# Step 10: If there are no options available (definitely possible), start over with with the inputs of step 2.
# Step 11: When the len(list of collapsed cells) == grid row x grid col, the map is complete

WATER = 'W'
COAST = 'C'
GRASS = 'G'

class Tile:
    def __init__(self):
        self.tile_type = None

def print_grid(grid: list[list[Tile | None]]):
    print_text = "Printing the grid:"
    print(print_text)
    print('-' * len(print_text))

    for col in grid:
        for row in col:
            if row.tile_type: # if it exists/not None
                print(row.tile_type, end=" ")
            else:
                print("-", end=" ")
        print()
    print()

def main():
    grid: list[list[Tile | None]] = [[Tile() for col in range(6)] for row in range(6)] # I learned that | means or, so I can make it a tile or none!
    print_grid(grid)

if __name__ == "__main__":
    main()