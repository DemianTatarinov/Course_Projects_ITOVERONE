# Напишите рекурсивную функцию,
# которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел,
# каждое в диапазоне от 1 до 100

from random import randint
a = [randint(1, 100) for i in range(10)]
print(a)
def Sum(a):
    if len(a) == 0:
        return 0
    else:
        return Sum(a[:-1]) + a[-1]
print(sum(a))