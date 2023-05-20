import pygame
import map_rendering
from player import Player
import game_map as map

# Добавьте остальной функционал, ранее находившийся в функции
# test_map_rendering()
def main():
    pygame.init()

    # Создание окна
    screen = pygame.display.set_mode(map_rendering.screen_size)

    # Создание объекта player
    player = Player()
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


# Запуск функции main()
if __name__ == "__main__":
    main()
