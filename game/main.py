import pygame
import random
from player import Player
from obstacle import Obstacle
from powerup import Powerup

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Red Ball Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FONT_SMALL = pygame.font.SysFont('Arial', 18)
FONT_MEDIUM = pygame.font.SysFont('Arial', 24)
FONT_LARGE = pygame.font.SysFont('Arial', 36)

PLAYER_SPEED = 5
PLAYER_GRAVITY = 0.5
PLAYER_JUMP_SPEED = 10

OBSTACLE_SPEED = 3

score = 0
game_over = False

player_image = pygame.image.load('E:\\МИРЭА\\python-proj-3sem\\game\\red_ball.png').convert_alpha()
obstacle_image = pygame.image.load('E:\\МИРЭА\\python-proj-3sem\\game\\blue_ball.png').convert_alpha()
background_image = pygame.image.load('E:\\МИРЭА\\python-proj-3sem\\game\\background.png').convert()

player = Player(50, WINDOW_HEIGHT - player_image.get_height())
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)

obstacles_group = pygame.sprite.Group()
for i in range(10):
    obstacle = Obstacle(obstacle_image, WINDOW_WIDTH, WINDOW_HEIGHT)
    obstacles_group.add(obstacle)
    all_sprites_group.add(obstacle)

powerups_group = pygame.sprite.Group()
for i in range(5):
    powerup = Powerup(RED, WINDOW_WIDTH, WINDOW_HEIGHT)
    powerups_group.add(powerup)
    all_sprites_group.add(powerup)

def game_over_screen():
    global game_over
    game_over = True
    text = FONT_LARGE.render('Game Over', True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    window.blit(text, text_rect)
    pygame.display.flip()

def win_screen():
    global game_over
    game_over = True
    text = FONT_LARGE.render('You Win!', True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    window.blit(text, text_rect)
    pygame.display.flip()

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_SPEED)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_SPEED)

    all_sprites_group.update()
    window.blit(background_image, (0, 0))
    all_sprites_group.draw(window)

    obstacles_hit_list = pygame.sprite.spritecollide(player, obstacles_group, False)
    for obstacle in obstacles_hit_list:
        game_over_screen()

    powerups_hit_list = pygame.sprite.spritecollide(player, powerups_group, True)
    for powerup in powerups_hit_list:
        score += 10

    if player.rect.right >= WINDOW_WIDTH:
        win_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
