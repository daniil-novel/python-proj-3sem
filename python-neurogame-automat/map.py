import random

# Константы для настройки карты
MAP_WIDTH = 50  # ширина карты
MAP_HEIGHT = 50  # высота карты
TRAP_COUNT = 10  # количество ловушек на карте
COMPLEXITY = 1  # сложность карты, от 0 до 1

# Объекты на карте
EMPTY = 0  # пустое место
WALL = 1  # стена
TRAP = 2  # ловушка
USER_SPAWN = 3  # точка спавна пользователя
NEURO_SPAWN = 4  # точка спавна нейросети
EXIT = 5

# Создание двумерного массива, заполненного пустыми местами
map_array = [[EMPTY for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

# Список точек спавна
spawn_points = []


def is_wall(x, y):
    """
    Функция проверяет, является ли клетка (x, y) на карте стеной.
    :param x: координата x клетки
    :param y: координата y клетки
    :return: True, если клетка является стеной, иначе False
    """
    if x < 0 or y < 0 or x >= MAP_WIDTH or y >= MAP_HEIGHT:
        # если координаты выходят за пределы карты, то считаем, что это стена
        return True
    else:
        return map_array[x][y] == WALL


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


def add_spawns():
    # добавляем точку спавна пользователя в левый верхний угол карты
    user_spawn_x = random.randint(3, 5)
    user_spawn_y = random.randint(3, 5)
    map_array[user_spawn_x][user_spawn_y] = USER_SPAWN
    spawn_points.append((user_spawn_x, user_spawn_y))

    # добавляем точку спавна нейросети в правый нижний угол карты
    neuro_spawn_x = MAP_WIDTH - random.randint(3, 25)
    neuro_spawn_y = MAP_HEIGHT - random.randint(3, 25)
    map_array[neuro_spawn_x][neuro_spawn_y] = NEURO_SPAWN
    spawn_points.append((neuro_spawn_x, neuro_spawn_y))


def add_level_exit():
    # Находим центр карты
    center_x = MAP_WIDTH // 2
    center_y = MAP_HEIGHT // 2

    # Находим координаты ближайшей точки спавна нейросети
    neuro_spawn_x = None
    neuro_spawn_y = None
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            if map_array[x][y] == NEURO_SPAWN:
                neuro_spawn_x = x
                neuro_spawn_y = y
                break
        if neuro_spawn_x is not None:
            break

    # Определяем, в какой половине карты находится нейросеть
    neuro_half = "left" if neuro_spawn_x < center_x else "right"

    # Выбираем случайную точку на той же стороне карты, где находится нейросеть
    if neuro_half == "left":
        exit_x = random.randint(5, center_x)
    else:
        exit_x = random.randint(center_x, MAP_WIDTH - 2)
    exit_y = random.randint(1, MAP_HEIGHT - 1)

    # Устанавливаем точку перехода на следующий уровень
    map_array[exit_x][exit_y] = EXIT


# Функция для отрисовки карты в терминале с помощью псевдографики
def map_init():
    # Добавляем стены на карту
    add_walls()

    # Добавляем ловушки на карту
    add_traps()

    # Добавляем точки спавна на карту
    add_spawns()

    # Добавляем точку перехода на следующий уровень
    add_level_exit()

def map_draw(map_array):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map_array[x][y] == WALL:
                print("#", end="")
            elif map_array[x][y] == TRAP:
                print("*", end="")
            elif map_array[x][y] == USER_SPAWN:
                print("U", end="")
            elif map_array[x][y] == NEURO_SPAWN:
                print("N", end="")
            elif map_array[x][y] == EXIT:
                print("E", end="")
            else:
                print(".", end="")
        print()


# Инициализация карту
map_init()
#map_draw(map_array)