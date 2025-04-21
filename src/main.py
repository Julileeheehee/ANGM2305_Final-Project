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
        self.display_surface.blit(self.surface_left, (PADDING, PADDING*2)) # Purple in picture
        self.display_surface.blit(self.surface_right, (PADDING*2 + GRID_WIDTH, PADDING*2)) # light blue in picture







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

        screen.fill(GRAY)
        panels.update()
        pygame.display.flip()
        clock.tick()

    pygame.quit()



if __name__ == "__main__":
    main()
