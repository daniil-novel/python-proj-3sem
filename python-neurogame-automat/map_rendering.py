import pygame
import map
from player import Player
from player import *

# Константы для настройки карты
SCREEN_WIDTH = 1000  # ширина экрана
SCREEN_HEIGHT = 1000  # высота экрана
TILE_SIZE = 20  # размер одного квадратика на карте
WALL_TEXTURE = pygame.image.load("wall_texture.png")  # текстура стен
ROAD_TEXTURE = pygame.image.load("road_texture1.png")  # текстура дороги


def set_screen_size(size):
    global screen_size
    screen_size = size


# Инициализация библиотеки pygame
pygame.init()

# Задаем размеры экрана
screen_size = (TILE_SIZE * 50, TILE_SIZE * 50)  # Здесь умножаем на 50,
# чтобы увеличить размер клеток в 50 раз
set_screen_size(screen_size)

# Создание окна
screen = pygame.display.set_mode(screen_size)

# Изменение размеров текстур для соответствия размеру клетки на карте
TEXTURE_SIZE = (20, 20)
wall_texture = pygame.transform.scale(WALL_TEXTURE, TEXTURE_SIZE)
road_texture = pygame.transform.scale(ROAD_TEXTURE, TEXTURE_SIZE)

# Функция для отрисовки карты на экране


def draw_map():
    for x in range(map.MAP_WIDTH):
        for y in range(map.MAP_HEIGHT):
            tile = map.map_array[x][y]
            tile_rect = pygame.Rect(
                x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Отрисовка текстуры для стен
            if tile == map.WALL:
                screen.blit(wall_texture, tile_rect)
            # Отрисовка текстуры для дороги
            elif tile == map.EMPTY:
                screen.blit(road_texture, tile_rect)
            # Отрисовка текстуры для ловушки
            elif tile == map.TRAP:
                pygame.draw.rect(screen, (255, 0, 0), tile_rect)
            elif tile == map.USER_SPAWN:
                pygame.draw.rect(screen, (50, 205, 50), tile_rect)
            elif tile == map.NEURO_SPAWN:
                pygame.draw.rect(screen, (50, 50, 255), tile_rect)
            elif tile == map.EXIT:
                pygame.draw.rect(screen, (255, 255, 255), tile_rect)

# Функция для тестирования отрисовки карты


def test_map_rendering():

    """
    # Добавление стен на карту
    map.add_walls()

    # Добавление ловушек на карту
    map.add_traps()

    # Добавление точек спавна на карту
    map.add_spawns()

    # Добавление точки перехода на следующий уровень
    map.add_level_exit()
    surface = map.map_init()
"""
    # Создание объекта player
    player = Player()
    clock = pygame.time.Clock()
    # Создание бесконечного цикла для отрисовки карты
    while True:
        # Обработка событий
        #player.y -= 10

        for event in pygame.event.get():
            player.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        player.update()  # добавляем вызов метода update()

        # Очистка экрана
        screen.fill((255, 255, 255))

        # Отрисовка карты
        draw_map()

        # Отрисовка игрока
        player.draw(screen)

        # Обновление экрана
        pygame.display.update()
        # Установка частоты кадров
        clock.tick(60)


# Запуск функции тестирования
test_map_rendering()
