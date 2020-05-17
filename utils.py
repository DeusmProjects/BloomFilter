import os
import random
import string
from BloomFilter import BloomFilter


COUNT_TEXTS = 200  # количество файлов
FP_PROB = 0.01  # желаемая вероятность ложного срабатывания
TEXTS_PATH = './texts'
FILTERS_PATH = './filters'


def create_texts():
    """
    Метод создания файлов со случайным текстом
    :return:
    """
    if not os.path.exists(TEXTS_PATH):
        os.mkdir(TEXTS_PATH)
    else:
        return

    for i in range(COUNT_TEXTS):
        write_file('file{}'.format(i))


def generate_random_string(length: int):
    """
    Генерация случайной строки, состоящей из строчных английских букв
    :param length: длина строки
    :return: str
    """
    return ''.join([random.choice(string.ascii_lowercase) for i in range(length)])


def write_file(name: str):
    """
    Запись текста в файл
    :param name: имя файла
    """
    count_words = random.randint(100, 200)
    words = [generate_random_string(random.randint(3, 8)) for i in range(count_words)]
    f = open(TEXTS_PATH + '/' + name, 'x')
    f.write(' '.join(words))
    f.close()


def init_filters():
    """
    Создание фильтра для каждого файла
    :return:
    """
    if not os.path.exists(FILTERS_PATH):
        os.mkdir(FILTERS_PATH)
    else:
        return

    for i in range(COUNT_TEXTS):
        f = open(TEXTS_PATH + '/file{}'.format(i), 'r')
        words = f.read().split(' ')
        f.close()
        bloom_filter = BloomFilter(len(words), FP_PROB)
        for word in words:
            bloom_filter.put(word)
        bloom_filter.save(FILTERS_PATH + '/filter{}'.format(i))
