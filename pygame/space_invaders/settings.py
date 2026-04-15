import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PLAYER_SPEED = 0.9
PLAYER_IMAGE_PATH = "img/spaceship.png"
PLAYER_SCALE = 0.5

ENEMY_DROP = 0.8
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED = 0.5
ENEMY_IMAGE_PATH = "img/alien1.png"
ENEMY_SCALE = 0.5
#Menu 
menu_font = pygame.font.SysFont("Arial", 50)
title_text = menu_font.render("SPACE INVADERS", True, (255, 255, 255),(255,0,0))
back_text = menu_font.render("BACK", True, (255, 255, 255),(255,0,0))
res1280_text = menu_font.render("1280x960", True, (255, 255, 255),(255,0,0))
res800_text = menu_font.render("800x600", True, (255, 255, 255),(255,0,0))
res1024_text = menu_font.render("1024x768", True, (255, 255, 255),(255,0,0))
play_text = menu_font.render("PLAY", True, (255, 255, 255),(255,0,0))
settings_text = menu_font.render("SETTINGS", True, (255, 255, 255),(255,0,0))
quit_text = menu_font.render("QUIT", True, (255, 255, 255),(255,0,0))

def update_rects():
    global title_rect, play_rect, settings_rect, quit_rect
    global res800_rect, res1024_rect, res1280_rect, back_rect
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 12))
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //3))
    settings_rect = settings_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
    res800_rect = res800_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    res1024_rect = res1024_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    res1280_rect = res1280_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 5 // 6))
update_rects()