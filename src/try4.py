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

class Tile():
    def __init__(self):
        #self.edges = []
        #self.north_possibilities = []
        #self.east_possibilities = []
        #self.south_possibilities = []
        #self.west_possibilities = []
        self.possibilities = TILES # A list
        self.collapsed = False

    def getNumofPossibilities(self):
        return len(self.possibilities)
    
    def analyze(self, tile):
        if tile == "W":
            self.possibilities = ["W", "C"]
        elif tile == "C":
            self.possibilities = ["W", "C", "G"]
        elif tile == "G":
            self.possibilities = ["C", "G"]
        else: #"n"
            self.possibilities = ["W", "C", "G"]
    
    def isCollapsed(self):
        if len(self.possibilities) == 1:
            self.collapsed = True
        return self.collapsed
    
    def showTile(self):
        return str(self.possibilities[0])
    
    def setTile(self, tiletobeset):
        tile = [tiletobeset]
        self.possibilities = tile
            


class Cell():
    def __init__(self, pos_x, pos_y):
        self.x = pos_x 
        self.y = pos_y # saves the location on the grid
        self.blank = "n"
        self.tile = Tile()
        self.entropy = self.tile.getNumofPossibilities() # Should start out with 3 in this case
        self.collapsed = False

    def setTile(self, tiletobeSet):
        self.collapsed = True
        self.tile.setTile(tiletobeSet)
        self.showTile()


    def showTile(self):
        if self.tile.isCollapsed() == False:
            self.collapsed = False
            return self.blank
        else:
            collapsedTile = self.tile.showTile()
            return collapsedTile
        
    def getEntropy(self):
        print(self.entropy)
    
    #def setToBlank(self):
     #   self.collapsed = False
    
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
            cell = Cell(i, j)
            grid[i][j] = cell.showTile()
    print('\n'.join(map(' '.join, grid)))

    first_coord = pickFirstCell()
    collapsed_tile = pickFirstTile()
    row = first_coord[0]
    col = first_coord[1]


    grid[row][col] = cell.setTile(collapsed_tile)
    grid[row][col] = cell.showTile()
    #print(grid)
    print('\n'.join(map(' '.join, grid)))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = cell.showEntropyNum() 

    print('\n'.join(map(' '.join, grid)))

    #showentropy(grid, cell)
    

def showentropy(grid, cell: Cell):
    entropy = ""
    for i in range(len(grid)):
       for j in range(len(grid[i])):
            grid[i][j] = cell.getEntropy()
            grid[i][j] = cell.showEntropyNum()
    print('\n'.join(map(' '.join, grid)))

def findNeighbors(coord_row, coord_col, grid_row, grid_col):
    north = None
    if coord_row != 0:
        north = [coord_row - 1,coord_col]

    east = None
    if coord_col != grid_col - 1:
        east = [coord_row, coord_col + 1]

    south = None
    if coord_row != grid_row - 1:
        south = [coord_row + 1,coord_col]

    west = None
    if coord_col != 0:
        west = [coord_row,coord_col - 1]
    
    listofNeighbors = [north,east,south,west]
    return listofNeighbors #<---------------------- Returns a 2D list 

def updateNeighborPossibilities(collapsed_tile, list_of_neighbors, grid):
    # Take the collapsed tile and compare it to 
    pass

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