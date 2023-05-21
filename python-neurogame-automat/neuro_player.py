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

    def handle_key_press(player, key):
        if key == pygame.K_w:
            player.move_up_flag = True
        elif key == pygame.K_s:
            player.move_down_flag = True
        elif key == pygame.K_a:
            player.move_left_flag = True
        elif key == pygame.K_d:
            player.move_right_flag = True

    def handle_key_release(player,key):
        if key == pygame.K_w:
            player.move_up_flag = False
        elif key == pygame.K_s:
            player.move_down_flag = False
        elif key == pygame.K_a:
            player.move_left_flag = False
        elif key == pygame.K_d:
            player.move_right_flag = False

    def get_collision_bounds(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)