import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
import random

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
player_bullet_group = pygame.sprite.Group()

enemy = Enemy(0,50)
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

SPAWN_EBULLET = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EBULLET, 2000)

def create_enemies():
    x = 50
    y = 25
    for i in range(2):
        for j in range(10):
            enemy = Enemy(x,y)
            x += 50
            enemy_group.add(enemy)
        y += 50
        x = 50
create_enemies()
        

running = True
while running:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE and player.cooldown == 0:
                bullet = Bullet(player.rect.left + 5,player.rect.top + 40, "Player")
                player_bullet_group.add(bullet)
                bullet = Bullet(player.rect.right - 5,player.rect.top + 40, "Player")
                player_bullet_group.add(bullet)
                player.cooldown = pygame.time.get_ticks()
        if event.type == SPAWN_EBULLET:
            for enemy in enemy_group:
                if random.randint(1,100) <= 20:
                    bullet = Bullet(enemy.rect.centerx,enemy.rect.bottom)
                    enemy_bullet_group.add(bullet)
        
    if pygame.sprite.groupcollide(player_group, enemy_group, True, True,pygame.sprite.collide_mask):
        print("srazka")
        running = False
    if pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True,pygame.sprite.collide_mask):
        print("srazka s player")
        running = False
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True,pygame.sprite.collide_mask):
        print("srazka s enemy")    

    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)

    player_bullet_group.update()
    player_bullet_group.draw(screen)

    enemy_group.update()
    enemy_group.draw(screen)

    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    pygame.display.flip()
pygame.quit()

