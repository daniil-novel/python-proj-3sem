import sys

import pygame
import random

# Размеры окна
WIDTH = 600
HEIGHT = 600

# Количество клеток в лабиринте
CELLS_X = 20
CELLS_Y = 20

# Размер клетки
CELL_SIZE = WIDTH // CELLS_X

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Класс, представляющий каждую клетку лабиринта
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]  # up, right, down, left
        self.visited = False

    # Отображение клетки
    def display(self):
        x = self.x * CELL_SIZE
        y = self.y * CELL_SIZE
        if self.visited:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            if self.walls[0]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 1)
            if self.walls[1]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if self.walls[2]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if self.walls[3]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 1)
# Создание лабиринта
def create_maze(width, height):
    # Создаем сетку клеток
    grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
    # Создаем список всех стен в лабиринте
    walls = []
    for x in range(width):
        for y in range(height):
            if x > 0:
                walls.append((x, y, 3))  # Левая стена
            if y > 0:
                walls.append((x, y, 0))  # Верхняя стена

    # Случайным образом сортируем список стен
    random.shuffle(walls)

    # Объединяем клетки лабиринта
    for wall in walls:
        x, y, direction = wall
        if direction == 0:  # Верхняя стена
            cell1 = grid[x][y - 1]
            cell2 = grid[x][y]
        elif direction == 1:  # Правая стена
            cell1 = grid[x + 1][y]
            cell2 = grid[x][y]
        elif direction == 2:  # Нижняя стена
            cell1 = grid[x][y + 1]
            cell2 = grid[x][y]
        elif direction == 3:  # Левая стена
            cell1 = grid[x - 1][y]
            cell2 = grid[x][y]

        if not cell1.visited or not cell2.visited:
            cell1.walls[direction] = False
            cell2.walls[(direction + 2) % 4] = False
            cell1.visited = True
            cell2.visited = True

    return grid

# Отображение лабиринта
def display_maze_gui(grid):
    # Отображение всех клеток лабиринта
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y].display()

    # Обновление экрана
    pygame.display.update()


# Создание лабиринта
# Тестирование
maze = create_maze(50, 20)

# Отображение лабиринта
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    for row in maze:
        for cell in row:
            cell.display()
    pygame.display.update()
