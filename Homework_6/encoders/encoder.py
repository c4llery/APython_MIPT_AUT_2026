import json
import csv
import pickle
import cv2
import numpy as np

class HistEncoder:
    @staticmethod
    def encode(file_path, data):
        raise NotImplementedError()


class BinHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)


class TxtHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        with open(file_path, 'w') as f:
            f.write(str(data))


class JsonHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        if isinstance(data, np.ndarray):
            data = data.tolist()
        
        with open(file_path, 'w') as f:
            json.dump(data, f)


class CsvHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        # Записываем в CSV. Предполагаем, что data - это одномерный список чисел.
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in data:
                writer.writerow([item])


class ImageHistEncoder(HistEncoder):
    @staticmethod
    def encode(file_path, data):
        # Если data - это гистограмма (массив чисел), сохранить её как картинку напрямую нельзя.
        # Но если data - это само изображение (numpy array), то используем cv2.imwrite.
        # Для гистограмм обычно рисуют график. 
        # Оставим простой вариант: если это 2D массив, сохраняем как картинку.
        data_np = np.array(data, dtype=np.uint8)
        if len(data_np.shape) == 2:
            cv2.imwrite(file_path, data_np)
        else:
            raise ValueError("Данные не являются 2D изображением для сохранения в картинку")