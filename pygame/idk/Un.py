# import pygame module
import pygame

# import sys library
import sys

# initializing pygame
pygame.init()

clock = pygame.time.Clock()

# Set the window screen size
display_screen = pygame.display.set_mode((500, 500))

# add font style and size
base_font = pygame.font.Font(None, 40)


active = False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

 
    pygame.display.flip()
    clock.tick(60)