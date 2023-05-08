import random

# Константы для настройки карты
MAP_WIDTH = 50 # ширина карты
MAP_HEIGHT = 50 # высота карты
TRAP_COUNT = 10 # количество ловушек на карте
COMPLEXITY = 0.3 # сложность карты, от 0 до 1

# Объекты на карте
EMPTY = 0 # пустое место
WALL = 1 # стена
TRAP = 2 # ловушка

# Создание двумерного массива, заполненного пустыми местами
map_array = [[EMPTY for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

# Функция для добавления стен на карту
def add_walls():
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            if x == 0 or y == 0 or x == MAP_WIDTH - 1 or y == MAP_HEIGHT - 1:
                map_array[x][y] = WALL
            elif random.random() > COMPLEXITY:
                map_array[x][y] = WALL

# Функция для добавления ловушек на карту
def add_traps():
    for i in range(TRAP_COUNT):
        x = random.randint(1, MAP_WIDTH - 2)
        y = random.randint(1, MAP_HEIGHT - 2)
        map_array[x][y] = TRAP

# Функция для отрисовки карты в терминале с помощью псевдографики
def draw_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map_array[x][y] == EMPTY:
                print(".", end="")
            elif map_array[x][y] == WALL:
                print("#", end="")
            elif map_array[x][y] == TRAP:
                print("*", end="")
        print()
