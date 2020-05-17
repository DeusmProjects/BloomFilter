from BloomFilter import BloomFilter
import utils


utils.create_texts()
utils.init_filters()

while True:
    query = input()
    count_query = 0
    for i in range(utils.COUNT_TEXTS):
        bf = BloomFilter.load(utils.FILTERS_PATH + '/filter{}'.format(i))
        if bf.contains(query):
            count_query += 1

    print('В {} файлах найдено {} совпадений'.format(utils.COUNT_TEXTS, count_query))

