import tensorflow as tf
import numpy as np
import game_map
import neuro_player
import os


# Определение нейронной сети
class NeuralNetwork:
    def __init__(self):
        # Путь к файлу с весами модели
        self.weights_file = 'model_weights.txt'

        # Определение архитектуры сети
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(32, activation='relu', input_shape=(6,)),
            tf.keras.layers.Dense(32, activation='relu'), # TODO dropOut
            tf.keras.layers.Dense(4, activation='softmax')
        ])

        self.model.compile(optimizer='adam', loss='categorical_crossentropy',
                           metrics=['accuracy'])

        # Загрузка весов модели из файла
        if os.path.isfile(self.weights_file):
            self.model.load_weights(self.weights_file)

        # Счетчик эпох
        self.epoch_count = 0

        # Сохранение изначальных весов в файл
        self.save_weights()

    def train(self, input_data, target_data):
        # Преобразование целевых действий в формат one-hot векторов
        target_data_one_hot = tf.keras.utils.to_categorical(target_data,
                                                            num_classes=4)

        # Обучение сети на основе входных данных и целевых данных
        self.model.fit(input_data, target_data_one_hot, epochs=1,
                       verbose=False)
        self.model.reset_states()  # Сброс внутреннего состояния модели

        self.epoch_count += 1

        # Каждую 1000 итерацию сохраняем новые веса в файл
        if self.epoch_count % 1000 == 0:
            self.save_weights()

    def predict(self, input_data):
        # Применение обученной сети для предсказания действия на основе входных данных
        predictions = self.model.predict(np.array([input_data]))
        action = np.argmax(predictions[0])
        return action

    def save_weights(self):
        # Сохранение весов модели в файл
        self.model.save_weights(self.weights_file)

    def load_weights(self):
        # Загрузка весов модели из файла
        if os.path.isfile(self.weights_file):
            self.model.load_weights(self.weights_file)
