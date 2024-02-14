import pygame
import constants
import map_rendering
from neural_network import NeuralNetwork
from player import Player
from neuro_player import NeuroPlayer
import game_map as map
import numpy as np
import time
import random
# pylint: disable


def main():
    pygame.init()
    map.map_init()
    screen = pygame.display.set_mode(map_rendering.screen_size)

    game_over_image = pygame.image.load("game_over.png")
    game_over_image = pygame.transform.scale(
        game_over_image, map_rendering.screen_size)

    user_failed_image = pygame.image.load("user_failed.png")
    user_failed_image = pygame.transform.scale(
        user_failed_image, map_rendering.screen_size)

    player = Player(speed=2)
    neuro_player = NeuroPlayer(speed=2)
    clock = pygame.time.Clock()

    neural_network = NeuralNetwork()

    history = []  # Хранение истории движений игрока
    last_iteration_time = time.time()
    game_start_time = time.time()

    collided = False

    num_random_moves = 5  # Количество случайных ходов каждую итерацию

    iteration = 0
    epoch = 0

    while True:
        iteration += 1
        print(f"Iteration: {iteration}, Epoch: {epoch}")

        for event in pygame.event.get():
            player.handle_events(event)
            neuro_player.handle_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update()
        neuro_player.update()

        if map.check_level_exit(player):
            screen.blit(game_over_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            # Сохранение весов модели в текстовый файл
            neural_network.save_weights("model_weights.weights.h5")
            pygame.quit()
            return

        if not collided and player.get_collision_bounds().colliderect(neuro_player.get_collision_bounds()):
            collided = True
            screen.blit(user_failed_image, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            # Сохранение весов модели в текстовый файл
            neural_network.save_weights("model_weights.weights.h5")
            pygame.quit()
            return

        # Получение текущего состояния игры
        map_array = map.map_array

        # Получение входных данных (координаты игрока и информация о стенах)
        input_data = [
            neuro_player.x, neuro_player.y,
            map_array[neuro_player.cell_x][neuro_player.cell_y - 1],
            map_array[neuro_player.cell_x][neuro_player.cell_y + 1],
            map_array[neuro_player.cell_x - 1][neuro_player.cell_y],
            map_array[neuro_player.cell_x + 1][neuro_player.cell_y]
        ]

        # Применение нейронной сети для предсказания действия
        action = neural_network.predict(input_data)

        # Выполнение действия над NeuroPlayer'ом
        if action == 0:
            neuro_player.move_up()
        elif action == 1:
            neuro_player.move_down()
        elif action == 2:
            neuro_player.move_left()
        elif action == 3:
            neuro_player.move_right()

        # Выполнение случайных ходов
        for _ in range(num_random_moves):
            random_action = random.randint(0, 3)
            if random_action == 0:
                neuro_player.move_up()
            elif random_action == 1:
                neuro_player.move_down()
            elif random_action == 2:
                neuro_player.move_left()
            elif random_action == 3:
                neuro_player.move_right()

        # Получение нового состояния игры после выполнения действия
        new_map_array = map.map_array

        # Получение новых входных данных (координаты игрока и информация о стенах)
        new_input_data = [
            neuro_player.x, neuro_player.y,
            new_map_array[neuro_player.cell_x][neuro_player.cell_y - 1],
            new_map_array[neuro_player.cell_x][neuro_player.cell_y + 1],
            new_map_array[neuro_player.cell_x - 1][neuro_player.cell_y],
            new_map_array[neuro_player.cell_x + 1][neuro_player.cell_y]
        ]

        # Вычисление вознаграждения и штрафов
        reward = 0
        if player.get_collision_bounds().colliderect(neuro_player.get_collision_bounds()):
            reward = 1  # Вознаграждение при касании пользователя
        elif neuro_player.is_approaching(player):
            reward += 0.015  # Вознаграждение при приближении к пользователю
        elif neuro_player.check_wall_collision(map.map_array):
            reward -= 0.005  # Штраф за касание стенок

        # Добавляем текущее состояние, действие и вознаграждение в историю
        history.append((input_data, action, reward))

        if time.time() - last_iteration_time >= 1:
            # Подготовка данных для обучения
            input_data_history = np.array([data[0] for data in history])
            action_history = np.array([data[1] for data in history])
            reward_history = np.array([data[2] for data in history])

            # Обновление весов нейронной сети на основе истории
            neural_network.train(input_data_history, reward_history)

            # Очищаем историю после обучения
            history = []

            # Обновляем время последней итерации
            last_iteration_time = time.time()

        screen.fill((255, 255, 255))
        map_rendering.draw_map()
        player.draw(screen)
        neuro_player.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
