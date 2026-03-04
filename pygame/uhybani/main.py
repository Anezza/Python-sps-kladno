import pygame
from Player import *
from settings import *
from Block import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

hrac = Player(WIDTH // 2, HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)

blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)
ADD_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_BLOCK, 2000)

while running:
    screen.fill((25,25,112))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    if pygame.sprite.spritecollide(hrac,blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE")
        running = False

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()