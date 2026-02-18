# import pygame module
import pygame

# import sys library
import sys

# initializing pygame
pygame.init()

clock = pygame.time.Clock()

# Set the window screen size
screen = pygame.display.set_mode((500, 500))

# add font style and size
base_font = pygame.font.Font(None, 40)
bomb_timer = 5
text = "Bomba vybuchne za : {}".format(bomb_timer)
# stores text taken by keyboard
bomb_timer_text = base_font.render(text, True, (255, 0, 0))
bomb_timer_text_rect = bomb_timer_text.get_rect(center=(250, 250))

active = False

while True:
    screen.blit(bomb_timer_text, bomb_timer_text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bomb_timer+=5
    screen.fill((255,255,255))
    text = "Bomba vybuchne za : {}".format(bomb_timer)
    bomb_timer_text = base_font.render(text, True, (0, 0, 0))
    screen.blit(bomb_timer_text, bomb_timer_text_rect)
    bomb_timer -= 1
    if bomb_timer < 0:
        break
    pygame.display.flip()
    clock.tick(1)