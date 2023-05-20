import pygame
import constants
import game_map as map
from player import Player


def set_screen_size(size):
    global screen_size
    screen_size = size


# Инициализация библиотеки pygame
pygame.init()

# Задаем размеры экрана
screen_size = (constants.TILE_SIZE * 50, constants.TILE_SIZE * 50)
set_screen_size(screen_size)

# Создание окна
screen = pygame.display.set_mode(screen_size)

# Изменение размеров текстур для соответствия размеру клетки на карте
TEXTURE_SIZE = (20, 20)
wall_texture = pygame.transform.scale(constants.WALL_TEXTURE, TEXTURE_SIZE)
road_texture = pygame.transform.scale(constants.ROAD_TEXTURE, TEXTURE_SIZE)


def draw_map():
    for x in range(constants.MAP_WIDTH):
        for y in range(constants.MAP_HEIGHT):
            tile = map.map_array[x][y]
            tile_rect = pygame.Rect(
                x * constants.TILE_SIZE,
                y * constants.TILE_SIZE,
                constants.TILE_SIZE,
                constants.TILE_SIZE)

            # Отрисовка текстуры для стен
            if tile == constants.WALL:
                screen.blit(wall_texture, tile_rect)
            # Отрисовка текстуры для дороги
            elif tile == constants.EMPTY:
                screen.blit(road_texture, tile_rect)
            # Отрисовка текстуры для ловушки
            elif tile == constants.TRAP:
                pygame.draw.rect(screen, (255, 0, 0), tile_rect)
            elif tile == constants.USER_SPAWN:
                pygame.draw.rect(screen, (50, 205, 50), tile_rect)
            elif tile == constants.NEURO_SPAWN:
                pygame.draw.rect(screen, (50, 50, 255), tile_rect)
            elif tile == constants.EXIT:
                pygame.draw.rect(screen, (255, 255, 255), tile_rect)
