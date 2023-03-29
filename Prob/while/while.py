number = 55
running = True
while running:
    guess = int(input('Введитк целое число:'))
    if guess == number:
         print('Поздравляю, вы угадали')
         running = False # это останавливает цикл
    elif guess < number:
        print('Нет,загаданное число немного больше этого. ')
    else:
        print('Нет, загаданное число меньше этого.')
else:
    print('Цикл while закончен.')
print('Завершение.')