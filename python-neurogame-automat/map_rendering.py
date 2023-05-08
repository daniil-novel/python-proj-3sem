import pygame
from pygame.locals import *
from map import *

# Константы для отображения карты
CELL_SIZE = 15
WINDOW_WIDTH = MAP_WIDTH * CELL_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * CELL_SIZE

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализация Pygame
pygame.init()

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Map Rendering Test")

# Функция отрисовки карты
def draw_map(map_array):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map_array[x][y] == WALL:
                pygame.draw.rect(window, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif map_array[x][y] == TRAP:
                pygame.draw.rect(window, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(window, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Функция тестирования
def main():
    # Создание карты
    add_walls()
    add_traps()

    # Отрисовка карты
    draw_map(map_array)

    # Отображение окна
    pygame.display.update()

    # Ожидание закрытия окна
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
