# Калькулятор: Пользователь вводит с клавиатуры число и операцию и получает результат

a = float(input("Введите дробное число: "))
c = input("Введите операцию(+,*,/,-): ")
b = float(input("Ведите второе дробное число: "))

if c=='+':
    print(a+b)
elif c=="=":
    print(a-b)
elif c=="*":
    print(a*b)
else:
    print(a/b)
