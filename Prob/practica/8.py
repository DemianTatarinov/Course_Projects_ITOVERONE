# Калькулятор.Создайте класс,
# где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

class Calc:
    def __init__(self):
        self.vvod()

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def dele(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def umn(self):
        return self.a * self.b

    def vvod(self):
        self.a = int(input("Введите 1 число: "))
        self.b = int(input("Введите 2 число: "))


while True:
    ex = Calc()
    c = input("Введите операцию (+,*,/,-):")
    if c == '+':
        print(ex.plus())
    elif c == '-':
        print(ex.minus())
    elif c == '*':
        print(ex.umn())
    elif c == '0':
        break
    else:
        print(ex.dele())