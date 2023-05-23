import random
import map_rendering
import constants



# Создание двумерного массива, заполненного пустыми местами
map_array = [[constants.EMPTY for y in range(constants.MAP_HEIGHT)] for x in range(constants.MAP_WIDTH)]

# Список точек спавна
spawn_points = []


def convert_to_cell(x, y):
    cell_x = x // constants.TILE_SIZE
    cell_y = y // constants.TILE_SIZE
    return cell_x, cell_y
# преобразовывает пиксельные значения в значения блока (n-ый блок
# относительно границ экрана)


def is_wall(x, y):
    cell_x, cell_y = convert_to_cell(x, y)
    return map_array[cell_x][cell_y] == constants.WALL


def add_walls():
    for x in range(constants.MAP_WIDTH):
        for y in range(constants.MAP_HEIGHT):
            if x == 0 or y == 0 or x == constants.MAP_WIDTH - 1 or y == constants.MAP_HEIGHT - 1:
                map_array[x][y] = constants.WALL
            elif random.random() < constants.COMPLEXITY:
                map_array[x][y] = constants.WALL


def add_traps():
    for i in range(constants.TRAP_COUNT):
        x = random.randint(1, constants.MAP_WIDTH - 2)
        y = random.randint(1, constants.MAP_HEIGHT - 2)
        map_array[x][y] = constants.TRAP

def check_level_exit(player):
    cell_x, cell_y = convert_to_cell(player.x, player.y)
    if map_array[cell_x][cell_y] == constants.EXIT:
        return True
    return False


def add_spawns():
    user_spawn_x = random.randint(4, 14)
    user_spawn_y = random.randint(2, 16)
    map_array[user_spawn_x][user_spawn_y] = constants.USER_SPAWN
    spawn_points.append((user_spawn_x, user_spawn_y))

    neuro_spawn_x = constants.MAP_WIDTH - random.randint(3, 25)
    neuro_spawn_y = constants.MAP_HEIGHT - random.randint(3, 25)
    map_array[neuro_spawn_x][neuro_spawn_y] = constants.NEURO_SPAWN
    spawn_points.append((neuro_spawn_x, neuro_spawn_y))


def add_level_exit():
    center_x = constants.MAP_WIDTH // 2
    center_y = constants.MAP_HEIGHT // 2

    neuro_spawn_x = None
    neuro_spawn_y = None
    for x in range(constants.MAP_WIDTH):
        for y in range(constants.MAP_HEIGHT):
            if map_array[x][y] == constants.NEURO_SPAWN:
                neuro_spawn_x = x
                neuro_spawn_y = y
                break
        if neuro_spawn_x is not None:
            break

    neuro_half = "left" if neuro_spawn_x < center_x else "right"

    if neuro_half == "left":
        exit_x = random.randint(5, center_x)
    else:
        exit_x = random.randint(center_x, constants.MAP_WIDTH - 2)
    exit_y = random.randint(1, constants.MAP_HEIGHT - 1)

    map_array[exit_x][exit_y] = constants.EXIT


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
    for y in range(constants.MAP_HEIGHT):
        for x in range(constants.MAP_WIDTH):
            if map_array[x][y] == constants.WALL:
                print("#", end="")
            elif map_array[x][y] == constants.TRAP:
                print("*", end="")
            elif map_array[x][y] == constants.USER_SPAWN:
                print("U", end="")
            elif map_array[x][y] == constants.NEURO_SPAWN:
                print("N", end="")
            elif map_array[x][y] == constants.EXIT:
                print("E", end="")
            elif map_array[x][y] == constants.EMPTY:
                print(".", end="")
        print()



# Инициализация карту
#map_init()
#map_draw(map_array)
# map_draw(map_array)
