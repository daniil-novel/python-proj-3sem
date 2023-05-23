# constants.py
import pygame

# Константы модуля map
MAP_WIDTH = 50  # ширина карты
MAP_HEIGHT = 50  # высота карты
TRAP_COUNT = 10  # количество ловушек на карте
COMPLEXITY = 0.1  # сложность карты, от 0 до 1

# Объекты на карте
EMPTY = 0  # пустое место
WALL = 1  # стена
TRAP = 2  # ловушка
USER_SPAWN = 3  # точка спавна пользователя
NEURO_SPAWN = 4  # точка спавна нейросети
EXIT = 5

# Константы модуля map_rendering
SCREEN_WIDTH = 1000  # ширина экрана
SCREEN_HEIGHT = 1000  # высота экрана
TILE_SIZE = 20  # размер одного квадратика на карте
WALL_TEXTURE = pygame.image.load("wall_texture.png")  # текстура стен
ROAD_TEXTURE = pygame.image.load("road_texture1.png")  # текстура дороги
