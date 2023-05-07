import pygame
import random

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('star.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 5
        if self.rect.y > 480:
            self.rect.y = -self.rect.height
            self.rect.x = random.randrange(0, 640 - self.rect.width)
