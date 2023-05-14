import math
import pygame

class Player:
    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y

    def move_up(self):
        if map.is_wall(self.x, self.y - 1):
            print("Cannot move up, there is a wall.")
        else:
            self.y -= 1

    def move_down(self):
        if map.is_wall(self.x, self.y + 1):
            print("Cannot move down, there is a wall.")
        else:
            self.y += 1

    def move_left(self):
        if map.is_wall(self.x - 1, self.y):
            print("Cannot move left, there is a wall.")
        else:
            self.x -= 1

    def move_right(self):
        if map.is_wall(self.x + 1, self.y):
            print("Cannot move right, there is a wall.")
        else:
            self.x += 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.move_right()

    def draw(self, screen):
        # определяем цвет и размер игрока
        color = (0, 128, 255)
        radius = 10

        # определяем координаты вершин шестиугольника
        points = [
            (self.x + radius * math.cos(0), self.y + radius * math.sin(0)),
            (self.x + radius * math.cos(1 * math.pi / 3),
             self.y + radius * math.sin(1 * math.pi / 3)),
            (self.x + radius * math.cos(2 * math.pi / 3),
             self.y + radius * math.sin(2 * math.pi / 3)),
            (self.x + radius * math.cos(math.pi),
             self.y + radius * math.sin(math.pi)),
            (self.x + radius * math.cos(4 * math.pi / 3),
             self.y + radius * math.sin(4 * math.pi / 3)),
            (self.x + radius * math.cos(5 * math.pi / 3),
             self.y + radius * math.sin(5 * math.pi / 3))
        ]

        # рисуем шестиугольник
        pygame.draw.polygon(screen, color, points)
