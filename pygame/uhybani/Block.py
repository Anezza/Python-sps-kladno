import pygame
from settings import *
import random
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randrange(0 + (B_WIDTH // 2), WIDTH - (B_WIDTH // 2))
        y = 0
        self.image = pygame.image.load(B_IMAGE_PATH).convert_alpha()
        self.image = pygame.image.load("obrazky/asteroid.png")
        self.image = pygame.transform.scale(self.image, (B_WIDTH,B_HEIGHT))
        self.rect = self.image.get_rect(bottom=y, centerx=x)
        self.speed = PLAYER_SPEED
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT + 100:
            self.kill()
if __name__ == "__main__":
    import main
