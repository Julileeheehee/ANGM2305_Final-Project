import pygame

GRID_X = 2 # tiles
GRID_Y = 2

TILESIZE = 64 # I made my tiles 64x64. Not sure why lmao

SCALE = 3

# Tile types
# The number is the id of the image(idk)
WATER_TILE = 0
COASTLINE_TILE = 1
GRASS_TILE = 2

# Note: I'm doing this because I know I'll need it later
tileEdges = {
    WATER_TILE : ["water", "water", "water", "water"],
    COASTLINE_TILE : ["coast", "coast", "coast", "coast"],
    GRASS_TILE : ["grass", "grass", "grass", "grass"]
}


def main():
    pygame.init()
    pygame.display.set_caption("3 Tile Test")
    screen = pygame.display.set_mode((GRID_X * TILESIZE * SCALE, GRID_X * TILESIZE * SCALE))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()