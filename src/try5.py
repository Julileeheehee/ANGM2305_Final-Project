import random

TILES = ["W", "C", "G"]

TILERULES = {
    'W': ["W", "W", "W", "W"],
    'C': ["C", "C", "C", "C"],
    'G': ["G", "G", "G", "G"]
}

NORTH = 0
EAST = 1
WEST = 2
SOUTH = 3


# class Grid():
'''
This class will be a 2D list that will store coordinates.
It will calculate neighbors and display info.
Each spot [i][j] will contain a Cell()
'''

# class Cell():
'''
This class will contain a list that will store the different tiles (own separate objects).
This class will calculate entropy and chooses the tiles to display
'''

# to simplify things for me, I won't make the tiles into its own class.

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







def main():
    pass


if __name__ == "__main__":
    main()