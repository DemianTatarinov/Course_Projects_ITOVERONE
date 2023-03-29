#Родительский класс
class Phone:

   #Инициализатор
   def __init__(self):
      self.is_on = False
   #Вкючаем телефон
   def turn_on(self):
      self.is_on = True
   #Если выключен телефон, делаем звонок
   def call(self):
      if self.is_on:
         print('Making call...')
#Унаследованный класс
class MobilePhone(Phone):
   #Добавляем новое свойства battery
   def __init__(self):
      super().__init__()
      self.battery = 0

#Заряжаем телефон на велечину переданного знаения
   def chage(self,num):
      self.battery = num
      print(f'Charging battary up to ... {self.battery}%')
my_mobile_phone = MobilePhone()
print(dir(my_mobile_phone))

#создаём класс Vihicle
class Vihicle:
   def vehicle_method(self):
      print("Это родительский метод из класса Vehicle")

#создаём класс Cycle, который унаследует Vehicle
class Car(Vihicle):
   def car_method(self):
      print("Это дочерний метод из класса Car")

#создаём класс Cycle, который наследует Vehicle
class Cycle(Vihicle):
   def cycleMethod(self):
      print("Это дочерний метод из класса Cycle")

car_a = Car()
car_a.vehicle_method()#вызов метода родительского класса
car_b = Cycle()
car_b.vehicle_method()#вызов метода родительского класса

class Camera:
   def camera_method(self):
      print("Это родительский метод из класса Camera")

class Radio:
   def radio_method(self):
      print("Это родительский метод из класса Radio")

class CellPhone(Camera, Radio):
   def cell_phone_method(self):
      print("Это дочерний метод из класса CellPhone")

cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()