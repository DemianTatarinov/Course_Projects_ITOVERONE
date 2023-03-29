# создайте кордеж из 10 чисел
# найдите индекс max() and min() элемента


import random
a = [random.randint(1,100) for i in range(10)]
a = tuple(a)
print(a)
print(a.index(min(a)),a.index(max(a)))
