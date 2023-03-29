# Допишите по 2 динамических и статических свойства
# в класс с предыдущего задания.
# Продемонстрируйте их работу

class Car:
   # Статические поля (переменные класса)
   default_color = 'Grey'
   default_weight = 5000
   default_speed = 300
   default_run = 10000

   def __init__(self,color,model,speed,run):
      # Динамические поля(переменные объекта)
      self.color = color
      self.model = model
      self.speed = speed
      self.run = run


   # def turn_on(self):
   #    pass
   # def ride(self):
   #    pass
car_object = Car('Red','BMW','250','20000')
print(car_object.default_color, car_object.default_weight, car_object.default_speed,car_object.default_run )
print(car_object.color, car_object.model, car_object.speed, car_object.run)
# print(dir(Car))