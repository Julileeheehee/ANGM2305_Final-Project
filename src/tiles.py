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
class Tiles:
    def __init__(self, tileIndex, x, y):
        self.index = tileIndex
        self.gridcopy = [[0 for row in range(GRID_X)] for col in range(GRID_Y)]
        self.gridlocation = self.gridcopy[x][y]

        self.possibilities = [WATER_TILE, COASTLINE_TILE, GRASS_TILE]
        self.entropy = len(self.possibilities) #should be 3 at the start





























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
                pygame.Surface.blit(screen, blank_tile, (i*tilesize, j*tilesize))
        
        grid[0][0] = pygame.Surface.blit(screen, tileImages[0], (0, 0))

        print("[0][0] entropy: ")
        print("[0][1] entropy: ")
        print("[1][0] entropy: ")
        print("[1][1] entropy: ")





















        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()