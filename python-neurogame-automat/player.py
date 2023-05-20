import math
import pygame
import game_map as map
import time


def print_player_coordinates(player):
    while True:
        print(f"Player coordinates: ({player.x}, {player.y})")
        time.sleep(1)


class Player:
    def __init__(self, x=110, y=210):
        self.x = x
        self.y = y
        self.move_up_flag = False
        self.move_down_flag = False
        self.move_left_flag = False
        self.move_right_flag = False

    def move_up(self):
        if map.is_wall(self.x, self.y - 5):
            print("Cannot move up, there is a wall.")
            self.y += 5
        else:
            self.move_up_flag = False
            self.y -= 5

    def move_down(self):
        if map.is_wall(self.x, self.y + 5):
            print("Cannot move down, there is a wall.")
            self.y -= 5
        else:
            self.move_down_flag = False
            self.y += 5

    def move_left(self):
        if map.is_wall(self.x - 5, self.y):
            print("Cannot move left, there is a wall.")
            self.x += 5
        else:
            self.move_left_flag = False
            self.x -= 5

    def move_right(self):
        if map.is_wall(self.x + 5, self.y):
            print("Cannot move right, there is a wall.")
            self.x -= 5
        else:
            self.move_right_flag = False
            self.x += 5

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

    def draw(self, screen):
        # определяем цвет и размер игрока
        color = (255, 255, 255)
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

    def update(self):
        if self.move_up_flag:
            self.move_up()
        elif self.move_down_flag:
            self.move_down()
        elif self.move_left_flag:
            self.move_left()
        elif self.move_right_flag:
            self.move_right()
