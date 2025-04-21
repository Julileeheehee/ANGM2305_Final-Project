import pygame
import random
#import sys

from settings import *



def main():
    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GRAY)
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
