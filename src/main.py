import pygame
import random
#import sys

from settings import *


class Panels:
    def __init__(self):
        self.surface_left = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        pygame.Surface.fill(self.surface_left, WHITE)

        self.surface_right = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
        pygame.Surface.fill(self.surface_right, WHITE)

        self.display_surface = pygame.display.get_surface()

    def update(self):
        self.display_surface.blit(self.surface_left, (0,0)) # Purple in picture
        self.display_surface.blit(self.surface_right, (PADDING*2 + GRID_WIDTH, PADDING*2)) # light blue in picture



def draw_grid(screen):
    tile_size = GRID_WIDTH//3
    for row in range(0, GRID_WIDTH - 1, tile_size):
        for col in range(0, GRID_HEIGHT - 1, tile_size):
            rect = pygame.Rect(row, col, tile_size, tile_size)
            pygame.draw.rect(screen, BLACK, rect, 2)





def main():
    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    panels = Panels()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #backgrounds
        screen.fill(GRAY)
        panels.update()

        #draw
        draw_grid(screen)


        #flip display
        pygame.display.flip()
        clock.tick()

    pygame.quit()



if __name__ == "__main__":
    main()
