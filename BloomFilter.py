import math
import mmh3
import pickle
from bitarray import bitarray


class BloomFilter:
    def __init__(self, items_count: int, fp_prob):
        """
        Конструктор
        :param items_count: количество элементов
        :param fp_prob: желаемая вероятность ложного срабатывания
        """
        self.fp_prob = fp_prob
        self.size = self.__get_size(items_count, fp_prob)
        self.hash_count = self.__get_hash_count(self.size, items_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)  # заполняем массив нулями

    def put(self, item):
        """
        Метод добавления элемента
        :param item: string
        """
        indexes = []
        for f in range(self.hash_count):
            index = mmh3.hash(item, seed=f) % self.size
            indexes.append(index)
            self.bit_array[index] = True

    def contains(self, item: str):
        """
        Метод проверки наличия элемента
        :param item: string
        :return: bool
        """
        for f in range(self.hash_count):
            index = mmh3.hash(item, seed=f) % self.size
            if not self.bit_array[index]:
                return False

        return True

    def save(self, filename: str):
        """
        Сериализует класс в файл
        :param filename: имя файла
        """
        f = open(filename, 'wb')
        pickle.dump(self, f)
        f.close()

    @staticmethod
    def load(filename: str):
        """
        Десириализует данные из файла
        :param filename: имя файла
        :return: BloomFilter
        """
        f = open(filename, 'rb')
        return pickle.load(f)

    @staticmethod
    def __get_size(n, p):
        """
        Возвращает размер битового массива
        :param n:
        :param p: вероятность ложного срабатывания
        :return: int
        """
        m = -(n * math.log(p)) / (math.log(2)**2)
        return int(m)

    @staticmethod
    def __get_hash_count(m, n):
        """
        Возвращает количество хэш-функций
        :param m: размер битового массива
        :param n: число вставляемых элементов
        :return: int
        """
        k = (m / n) * math.log(2)
        return int(k)
