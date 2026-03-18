import pygame
from Player import *
from settings import *
from Block import *
import os
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

hrac = Player(WIDTH // 2, HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
#blok
blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)
SPAWN_BLOCK = pygame.USEREVENT + 1
spawning_timer = 2000
pygame.time.set_timer(SPAWN_BLOCK, spawning_timer)
base_font = pygame.font.Font(None, 40)
#score
score = 0
highscore = 0
text = "Score: {}".format(score)
score_text = base_font.render(text, True, (255, 0, 0))
score_text_rect = score_text.get_rect(topleft=(20, 20))
#highscore
highscoretext = "Highscore: {}".format(highscore)
highscore_text = base_font.render(highscoretext, True, (255, 0, 0))
highscore_text_rect = highscore_text.get_rect(topleft=(20, 50))

while running:
    screen.fill((25,25,112))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_BLOCK:
            blok_group.add(Block())
            score += 1
            if score % 2 == 0 and score !=0:
                spawning_timer = max(500, spawning_timer - 100)
                pygame.time.set_timer(SPAWN_BLOCK, spawning_timer)
        
    text = "Score: {}".format(score)
    score_text = base_font.render(text, True, (255, 0, 0))
    screen.blit(score_text, score_text_rect)

    highscoretext = "Highscore: {}".format(highscore)
    highscore_text = base_font.render(highscoretext, True, (255, 0, 0))
    screen.blit(highscore_text, highscore_text_rect)

    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)
    

    if pygame.sprite.spritecollide(hrac,blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE")
        if highscore <= score:
            with open('highscore.txt', 'w') as soubor:
                soubor.write(highscoretext)
            highscore = score
        running = False

    for blok in blok_group:
        if hrac.rect.bottom < blok.rect.top:
            score += 1
            highscore += 1
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()

