import sys
import pygame
import constants
import map_rendering
from player import Player
from neuro_player import NeuroPlayer  # Импортируем класс NeuroPlayer
import game_map as map

# Добавьте остальной функционал, ранее находившийся в функции
# test_map_rendering()
"""
def main():
    pygame.init()
    map.map_init()
    # Создание окна
    screen = pygame.display.set_mode(map_rendering.screen_size)

    # Создание объекта player
    player = Player(speed = 2)
    clock = pygame.time.Clock()

    # Создание бесконечного цикла для отрисовки карты
    while True:
        for event in pygame.event.get():
            player.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update()

        # Очистка экрана
        screen.fill((255, 255, 255))

        # Отрисовка карты из модуля map_rendering
        map_rendering.draw_map()

        # Отрисовка игрока
        player.draw(screen)

        # Обновление экрана
        pygame.display.update()

        # Установка частоты кадров
        clock.tick(60)

"""


def main():
    pygame.init()
    map.map_init()
    screen = pygame.display.set_mode(map_rendering.screen_size)

    game_over_image = pygame.image.load("game_over.png")
    game_over_image = pygame.transform.scale(game_over_image,
                                             map_rendering.screen_size)

    user_failed_image = pygame.image.load("user_failed.png")
    user_failed_image = pygame.transform.scale(user_failed_image,
                                               map_rendering.screen_size)

    player = Player(speed=5)
    neuro_player = NeuroPlayer(speed=2)
    clock = pygame.time.Clock()

    collided = False

    while True:
        for event in pygame.event.get():
            player.handle_events(event)
            neuro_player.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update()
        neuro_player.update()

        if map.check_level_exit(player):
            screen.blit(game_over_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            return

        if not collided and player.get_collision_bounds().colliderect(
                neuro_player.get_collision_bounds()):
            collided = True
            screen.blit(user_failed_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            return

        screen.fill((255, 255, 255))
        map_rendering.draw_map()
        player.draw(screen)
        neuro_player.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()