## Казино. Числа от 1 до 10 и цвета от 1 до 2( 1 - красный, 2 - чёрный).
# У пользователя 5 попыток

import random

a = random.randint(1,10)
b = random.randint(1,2)

i = 0

while 1<5:
    i += 1
    c = int(input("ВВедите число от 1 до 10: "))
    d = int(input("Введите цвет от 1 до 2 (1 - красный, 2 - чёрный): "))
    if a ==c and b ==d:
        print(f'Вы угадали фвет и число: {c}{d}')
        break
    elif a!=c and b == d:
        print(f'Вы не угадали число: {c}, но удали цвет: {d}')
    elif a ==c and b !=d:
        print(f'Вы не угадали число: {d}, но удали цвет: {c}')
    else:
        print(f'Вы не угадали цвет и число: {c}{d}, Ппробуёте ещё раз')
