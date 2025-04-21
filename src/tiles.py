import pygame

GRID_X = 2 # tiles
GRID_Y = 2

TILESIZE = 64 # I made my tiles 64x64. Not sure why lmao

SCALE = 3

# Tile types w/ index
WATER_TILE = 0
COASTLINE_TILE = 1
GRASS_TILE = 2

def loadImages():
    tiles = [
        pygame.transform.scale((pygame.image.load('images/3-tiles/water_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE)),
        pygame.transform.scale((pygame.image.load('images/3-tiles/coastline_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE)),
        pygame.transform.scale((pygame.image.load('images/3-tiles/grass_tile.png').convert_alpha()), (SCALE*TILESIZE, SCALE*TILESIZE)),
    ]
    return tiles

# Note: I'm doing this because I know I'll need it later
tileEdges = {
    WATER_TILE : ["water", "water", "water", "water"],
    COASTLINE_TILE : ["coast", "coast", "coast", "coast"],
    GRASS_TILE : ["grass", "grass", "grass", "grass"]
}

# makes the grid
grid = []

def main():
    pygame.init()
    pygame.display.set_caption("3 Tile Test")
    tilesize = TILESIZE * SCALE
    screen = pygame.display.set_mode((GRID_X * tilesize, GRID_X * tilesize))
    clock = pygame.time.Clock()
    tiles = loadImages()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #---------------add code below---------------
        for row in range(GRID_X):
            for col in range(GRID_Y):
                pygame.Surface.blit(screen, tiles[2], (row*tilesize, col*tilesize))





















        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()