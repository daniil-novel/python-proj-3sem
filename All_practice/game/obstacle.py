import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, x, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.height = height

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
