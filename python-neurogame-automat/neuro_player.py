import pygame
import game_map as map
import time
import constants

class NeuroPlayer:
    def __init__(self, x=610, y=310, speed=5, radius = 5):
        spawn_point = map.spawn_points[1]  # Берем точку спавна нейроигрока
        self.cell_x, self.cell_y = spawn_point
        self.x = (self.cell_x * constants.TILE_SIZE) + (constants.TILE_SIZE // 2)
        self.y = (self.cell_y * constants.TILE_SIZE) + (constants.TILE_SIZE // 2)
        self.speed = speed

        self.move_up_flag = False
        self.move_down_flag = False
        self.move_left_flag = False
        self.move_right_flag = False
        self.radius = radius

    def reset(self):
        spawn_point = map.spawn_points[1]
        self.cell_x, self.cell_y = spawn_point
        self.x = (self.cell_x * constants.TILE_SIZE) + (
                    constants.TILE_SIZE // 2)
        self.y = (self.cell_y * constants.TILE_SIZE) + (
                    constants.TILE_SIZE // 2)

        self.move_up_flag = False
        self.move_down_flag = False
        self.move_left_flag = False
        self.move_right_flag = False

    def move_up(self):
        if map.is_wall(self.x, self.y - self.speed):
            self.y += self.speed
        else:
            self.y -= self.speed

    def move_down(self):
        if map.is_wall(self.x, self.y + self.speed):
            self.y -= self.speed
        else:
            self.y += self.speed

    def move_left(self):
        if map.is_wall(self.x - self.speed, self.y):
            self.x += self.speed
        else:
            self.x -= self.speed

    def move_right(self):
        if map.is_wall(self.x + self.speed, self.y):
            self.x -= self.speed
        else:
            self.x += self.speed

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.move_up_flag = True
            elif event.key == pygame.K_s:
                self.move_down_flag = True
            elif event.key == pygame.K_a:
                self.move_left_flag = True
            elif event.key == pygame.K_d:
                self.move_right_flag = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.move_up_flag = False
            elif event.key == pygame.K_s:
                self.move_down_flag = False
            elif event.key == pygame.K_a:
                self.move_left_flag = False
            elif event.key == pygame.K_d:
                self.move_right_flag = False

    def update(self):
        if self.move_up_flag and self.move_left_flag:
            self.move_up_left()
        elif self.move_up_flag and self.move_right_flag:
            self.move_up_right()
        elif self.move_down_flag and self.move_left_flag:
            self.move_down_left()
        elif self.move_down_flag and self.move_right_flag:
            self.move_down_right()
        elif self.move_up_flag:
            self.move_up()
        elif self.move_down_flag:
            self.move_down()
        elif self.move_left_flag:
            self.move_left()
        elif self.move_right_flag:
            self.move_right()

    def move_up_left(self):
        if not map.is_wall(self.x - self.speed, self.y - self.speed):
            self.x -= self.speed
            self.y -= self.speed

    def move_up_right(self):
        if not map.is_wall(self.x + self.speed, self.y - self.speed):
            self.x += self.speed
            self.y -= self.speed

    def move_down_left(self):
        if not map.is_wall(self.x - self.speed, self.y + self.speed):
            self.x -= self.speed
            self.y += self.speed

    def move_down_right(self):
        if not map.is_wall(self.x + self.speed, self.y + self.speed):
            self.x += self.speed
            self.y += self.speed

    def draw(self, screen):
        # Определяем цвет и размер нейроигрока
        color = (255, 0, 0)
        radius = 5

        # Определяем координаты вершин шестиугольника
        points = [
            (self.x - radius, self.y - radius),  # Верхняя левая вершина
            (self.x + radius, self.y - radius),  # Верхняя правая вершина
            (self.x + radius, self.y + radius),  # Нижняя правая вершина
            (self.x - radius, self.y + radius)   # Нижняя левая вершина
        ]

        # Рисуем шестиугольник
        pygame.draw.polygon(screen, color, points)

    def is_approaching(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= 100

    def check_wall_collision(self, map_array):
        cell_x = int(self.x / constants.TILE_SIZE)
        cell_y = int(self.y / constants.TILE_SIZE)
        if map_array[cell_x][cell_y] == 1:
            return True
        return False

    def get_collision_bounds(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )