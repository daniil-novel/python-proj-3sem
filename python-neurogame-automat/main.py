import pygame
import map
from map_rendering import TILE_SIZE
from player import Player

pygame.init()

def main():
    '''# Создаем карту и добавляем на нее стены, ловушки, точки спавна и выход на следующий уровень
    map.add_walls()
    map.add_traps()
    map.add_spawns()
    map.add_level_exit()

    # Создаем игрока и устанавливаем его начальную позицию
    player = Player(50, 50)

    # Запускаем игровой цикл
    pygame.init()
    surface = pygame.display.set_mode((map.MAP_WIDTH * TILE_SIZE, map.MAP_HEIGHT * TILE_SIZE))
    clock = pygame.time.Clock()
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Перемещаем игрока к позиции, кликнутой мышью
                player.set_target(*event.pos)

        # Обновление состояния игры
        player.update()

        # Отрисовка состояния игры
        surface.fill((255, 255, 255))
        player.draw(surface)
        pygame.display.flip()

        # Ограничение частоты кадров
        clock.tick(60)

    pygame.quit()
    '''


if __name__ == '__main__':
    main()