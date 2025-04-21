import pygame
import random
#import sys

from settings import *


class Grid:
    def __init__(self):
        self.surface = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        pygame.Surface.fill(self.surface, WHITE)
        self.display_surface = pygame.display.get_surface()

    def update(self):
        self.display_surface.blit(self.surface, (PADDING, PADDING*2)) # surface, position

class Panel:
    def __init__(self):
        self.surface = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
        pygame.Surface.fill(self.surface, WHITE)
        self.display_surface = pygame.display.get_surface()

    def update(self):
        self.display_surface.blit(self.surface, (PADDING*2 + GRID_WIDTH, PADDING*2)) # surface, position







def main():
    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    grid = Grid()
    panel = Panel()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GRAY)
        grid.update()
        panel.update()
        pygame.display.flip()
        clock.tick()

    pygame.quit()



if __name__ == "__main__":
    main()
