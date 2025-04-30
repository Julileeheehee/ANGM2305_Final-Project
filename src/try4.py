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



class Cell():
    def __init__(self):
        self.blank = "n"
        self.tile = self.blank
        self.possibilities = TILES # Should start out with 3 in this case
        self.entropy = len(self.possibilities)
    
    def getEntropy(self):
        return str(self.entropy)
    
    def setToBlank(self):
        return self.blank
    
    def collapseCell(self, pickedTile):
        self.tile = pickedTile
        self.entropy = 0
        return self.tile
    
    def showEntropyNum(self):
        self.tile = self.getEntropy()
        return self.tile


"""def grid():
    #empty_cell = "n"
    
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = Cell()
            grid[i][j] = cell.setToBlank()
    print('\n'.join(map(' '.join, grid)))

    entropy_grid = grid
    for i in range(len(entropy_grid)):
       for j in range(len(entropy_grid[i])):

            entropy_grid[i][j] = cell.showEntropyNum()
    print('\n'.join(map(' '.join, entropy_grid)))

    first_coord = pickFirstCell()
    first_tile = pickFirstTile()
    first_row = first_coord[0]
    first_col = first_coord[1]

    grid[first_row][first_col] = cell.collapseCell(first_tile)
    print('\n'.join(map(' '.join, grid)))"""
    
def grid():
    
    
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            empty_cell = "n"
            grid[i][j] = empty_cell
    print('\n'.join(map(' '.join, grid)))

    
    

    first_coord = pickFirstCell()
    first_tile = pickFirstTile()
    first_row = first_coord[0]
    first_col = first_coord[1]

    grid[first_row][first_col] = first_tile
    print('\n'.join(map(' '.join, grid)))
    showentropy(grid)
    
def showentropy(grid):
    entropy = ""
    for i in range(len(grid)):
       for j in range(len(grid[i])):
            if grid[i][j] == "n":
                entropy = 3
            else:
                entropy = 0
            grid[i][j] = str(entropy)
    print('\n'.join(map(' '.join, grid)))

def pickFirstCell():
    row = int(input("Row? (0, 1, 2): "))
    col = int(input("Column? (0, 1, 2): "))

    first_coordinate = [row, col]
    return first_coordinate

def pickFirstTile():
    first_tile = input("Tile? (W, C, G): ")
    return first_tile


def main():
    grid()


if __name__ == "__main__":
    main()