import math
import pygame
import game_map as map
import time
import constants
"""
def print_player_coordinates(player):
    while True:
        print(f"Player coordinates: ({player.x}, {player.y})")
        time.sleep(1)
"""

class Player:
    def __init__(self, x=110, y=210, speed=5, radius=5):
        spawn_point = map.spawn_points[0]  # Берем точку спавна пользователя
        self.cell_x, self.cell_y = spawn_point
        self.x = (self.cell_x * constants.TILE_SIZE) + (
                    constants.TILE_SIZE // 2)
        self.y = (self.cell_y * constants.TILE_SIZE) + (
                    constants.TILE_SIZE // 2)

        self.speed = speed

        self.move_up_flag = False
        self.move_down_flag = False
        self.move_left_flag = False
        self.move_right_flag = False
        self.radius = radius

    def reset(self):
        spawn_point = map.spawn_points[0]
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
            print("Cannot move up, there is a wall.")
            self.y += self.speed
        else:
            self.y -= self.speed

    def move_down(self):
        if map.is_wall(self.x, self.y + self.speed):
            print("Cannot move down, there is a wall.")
            self.y -= self.speed
        else:
            self.y += self.speed

    def move_left(self):
        if map.is_wall(self.x - self.speed, self.y):
            print("Cannot move left, there is a wall.")
            self.x += self.speed
        else:
            self.x -= self.speed

    def move_right(self):
        if map.is_wall(self.x + self.speed, self.y):
            print("Cannot move right, there is a wall.")
            self.x -= self.speed
        else:
            self.x += self.speed

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_up_flag = True
            if event.key == pygame.K_DOWN:
                self.move_down_flag = True
            if event.key == pygame.K_LEFT:
                self.move_left_flag = True
            if event.key == pygame.K_RIGHT:
                self.move_right_flag = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.move_up_flag = False
            if event.key == pygame.K_DOWN:
                self.move_down_flag = False
            if event.key == pygame.K_LEFT:
                self.move_left_flag = False
            if event.key == pygame.K_RIGHT:
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
        if map.is_wall(self.x - self.speed, self.y - self.speed):
            print("Cannot move up-left, there is a wall.")
        else:
            self.x -= self.speed
            self.y -= self.speed

    def move_up_right(self):
        if map.is_wall(self.x + self.speed, self.y - self.speed):
            print("Cannot move up-right, there is a wall.")
        else:
            self.x += self.speed
            self.y -= self.speed

    def move_down_left(self):
        if map.is_wall(self.x - self.speed, self.y + self.speed):
            print("Cannot move down-left, there is a wall.")
        else:
            self.x -= self.speed
            self.y += self.speed

    def move_down_right(self):
        if map.is_wall(self.x + self.speed, self.y + self.speed):
            print("Cannot move down-right, there is a wall.")
        else:
            self.x += self.speed
            self.y += self.speed

    def draw(self, screen):
        # определяем цвет и размер игрока
        color = (200, 225, 255)
        radius = 5

        # определяем координаты вершин шестиугольника
        points = [
            (self.x - radius, self.y - radius),  # Верхняя левая вершина
            (self.x + radius, self.y - radius),  # Верхняя правая вершина
            (self.x + radius, self.y + radius),  # Нижняя правая вершина
            (self.x - radius, self.y + radius)  # Нижняя левая вершина
        ]

        # рисуем шестиугольник
        pygame.draw.polygon(screen, color, points)

    def get_collision_bounds(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

