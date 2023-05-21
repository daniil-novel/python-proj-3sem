import sys
import pygame
import constants
import map_rendering
from player import Player
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
    # Создание окна
    screen = pygame.display.set_mode(map_rendering.screen_size)

    # Загрузка картинки завершения игры и масштабирование ее
    game_over_image = pygame.image.load("game_over.png")
    game_over_image = pygame.transform.scale(game_over_image, map_rendering.screen_size)

    # Создание объекта player
    player = Player(speed=2)
    clock = pygame.time.Clock()

    # Создание бесконечного цикла для отрисовки карты
    while True:
        for event in pygame.event.get():
            player.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update()

        # Проверка достижения квадратика перехода на следующий уровень
        if map.check_level_exit(player):
            screen.blit(game_over_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)  # Задержка 2 секунды
            pygame.quit()
            return

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


# Запуск функции main()
if __name__ == "__main__":
    main()