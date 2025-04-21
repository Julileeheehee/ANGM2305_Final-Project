import pygame

#-------------------------------Constants--------------------------------------------
GRID_X = 2 # tiles
GRID_Y = 2

TILESIZE = 64 # I made my tiles 64x64. Not sure why lmao

SCALE = 3

# Directions clockwise
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Tile types w/ index
WATER_TILE = 0
COASTLINE_TILE = 1
GRASS_TILE = 2


# Note: I'm doing this because I know I'll need it later
tileEdges = {
    WATER_TILE : ["water", "water", "water", "water"],
    COASTLINE_TILE : ["coast", "coast", "coast", "coast"],
    GRASS_TILE : ["grass", "grass", "grass", "grass"]
}

#---------------------------Classes (will move later)-----------------------------------------
class Tile:
    def __init__(self, listofneighbors):
        self.index = 0 # Just starts out as water lol
        self.neighbors = listofneighbors # ex: [1,0,1,1]
        self.possibilities = [WATER_TILE, COASTLINE_TILE, GRASS_TILE]
        self.entropy = len(self.possibilities) #should be 3 at the start
    
    def isCollapsed(self):
        collapsed = False
        if self.entropy == 1:
            collapsed = True
        return collapsed
    
    def getEntropy(self):
        return self.entropy
    
    def setInitialTile(self, tileType):
        self.index = tileType
        self.possibilities = [tileType]
        self.entropy = 1
    
    def getIndex(self):
        return self.index
        

class Cell:
    def __init__(self, x, y):
        self.row = x
        self.col = y
        self.gridcopy = [[0 for row in range(GRID_X)] for col in range(GRID_Y)]
        self.gridlocation = self.gridcopy[self.row][self.col]

        neighbors = self.getNeighbors()
        self.tile = Tile(neighbors)

    def getNeighbors(self):
        listofneighbors = []
        # Assume there are neighbors
        north = 1
        east = 1
        south = 1
        west = 1

        # first row
        if self.row == 0:
            # won't have a north neighbor
            north = 0

        # last row
        if self.row == GRID_X:
            # won't have a south neighbor
            south = 0

        # first col
        if self.col == 0:
            # won't have a west neighbor
            west = 0

        # last col
        if self.col == GRID_Y:
            #won't have an east neighbor
           east = 0
        
        listofneighbors = [north, east, south, west]
        return listofneighbors
    
    def isCollapsed(self):
        collapsed = self.tile.isCollapsed()
        return collapsed
    
    def getEntropy(self):
        return self.tile.getEntropy()
    
    def setInitialTile(self, tileType):
        self.tile.setInitialTile(tileType)
    
    def getIndex(self):
        return self.tile.getIndex()


    



























def displayEntropy(font, grid, screen):
    for y in range(GRID_Y):
        for x in range(GRID_X):
            text = (pygame.font.Font.render(font, str(grid[x][y].getEntropy()), True, (255,255,255)))
            pygame.Surface.blit(screen, text, ((x*TILESIZE * SCALE), y*TILESIZE * SCALE)) 



def loadImages():
    tileImages = [
        pygame.transform.scale((pygame.image.load('images/3-tiles/water_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE)),
        pygame.transform.scale((pygame.image.load('images/3-tiles/coastline_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE)),
        pygame.transform.scale((pygame.image.load('images/3-tiles/grass_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE))
    ]
    return tileImages


def main():
    pygame.init()
    pygame.display.set_caption("3 Tile Test")
    tilesize = TILESIZE * SCALE
    screen = pygame.display.set_mode((GRID_X * tilesize, GRID_X * tilesize))

    clock = pygame.time.Clock()
    tileImages = loadImages()
    blank_tile = pygame.transform.scale((pygame.image.load('images/3-tiles/blank_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE))
    font = pygame.font.Font(None, TILESIZE)
    collapsed = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #---------------add code below---------------

        #initializes a 2x2 grid??????
        grid = [[0 for row in range(GRID_X)] for col in range(GRID_Y)]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = Cell(i, j)
                #entropyNum = grid[i][j].getEntropy()
                #print(entropyNum)
                pygame.Surface.blit(screen, blank_tile, (i*tilesize, j*tilesize))
                #text = (pygame.font.Font.render(font, entropyNum, True, (255,255,255))).get_rect()
                #pygame.Surface.blit(screen, text, (i*tilesize, j*tilesize))

        
        # Forces the top left corner to be a water tile
        grid[0][0].setInitialTile(WATER_TILE)
        pygame.Surface.blit(screen, tileImages[grid[0][0].getIndex()], (0, 0))
        #print(type(grid[0][0].getEntropy()))

        displayEntropy(font, grid, screen)
        

        #entropy = grid[0][0].getEntropy()
        #print(entropy)


        #print(f"[0][0] entropy: {grid[0][0].getEntropy()}")
        #print(f"[0][1] entropy: {grid[0][1].getEntropy()}")
        #print(f"[1][0] entropy: {grid[1][0].getEntropy()}")
        #print(f"[1][1] entropy: {grid[1][1].getEntropy()}")





















        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()