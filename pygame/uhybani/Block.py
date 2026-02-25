import pygame
from settings import *
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("obrazky/asteroid.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HEIGHT))
        self.rect = self.image.get_rect(bottom=y, centerx=x)
        self.speed = PLAYER_SPEED


if __name__ == "__main__":
    import main
