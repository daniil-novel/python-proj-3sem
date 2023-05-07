import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('red_ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 640 - self.rect.width:
            self.rect.x = 640 - self.rect.width

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= self.level.height:
            self.change_y = -10

    def update(self):
        self.change_y += self.level.gravity

        self.rect.y += self.change_y

        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for platform in platform_hit_list:
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
            elif self.change_y < 0:
                self.rect.top = platform.rect.bottom

            self.change_y = 0
