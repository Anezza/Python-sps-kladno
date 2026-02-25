#import pygame module
import pygame

# import sys library
import sys

# initializing pygame
pygame.init()
a = 50
b = 200
vlevo = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
ball = pygame.image.load('obrazky/football.png')
ball = pygame.transform.scale(ball, (40, 40))
rotation_angle = 0
running = True

while running:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rotated_ball = pygame.transform.rotate(ball, rotation_angle)
    ball_rect = rotated_ball.get_rect(center=(a, b))

    screen.blit(rotated_ball, ball_rect)
    pygame.draw.line(screen, (255, 102, 0), [25, b+20], [370, b+20], 5)

    if vlevo:
        a-=1
        rotation_angle += 15
        if a <= 50:
            vlevo = False
    else:
        a += 1 
        rotation_angle -= 15
        if a >= 350:
            vlevo = True
    pygame.display.update()
pygame.quit()