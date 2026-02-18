#import pygame module
import pygame

# import sys library
import sys

# initializing pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.line(screen, (255, 0, 0), 
                 [100, 300], 
                 [500, 300], 5)

    pygame.draw.circle(screen, (0, 255, 0),
                   [280, 280], 20, 0)
    pygame.display.flip()
    clock.tick(60)