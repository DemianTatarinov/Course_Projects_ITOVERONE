# В саду сорвали цветы
# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# На лугу сорвали цветы
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Создайте множество цветов, произрастающих одновременно в саду и на лугу

garden = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',}
meadow = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',}
everywhere = garden|meadow
print(garden.union(meadow))
print(everywhere)
# print(type(garden))
# print(type(meadow))


# Проверить, есть ли в последовательности
# чисел списка дубликаты

# a = set([1,2,3,4,5,6,7,8,9,])
# b = set([9,8,7,6,5,4,3,2,1])
# print(a.isdisjoint(b))


