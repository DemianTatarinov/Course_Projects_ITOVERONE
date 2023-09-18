# создаём класс Vihicle
class Vihicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# создаём класс Cycle, который унаследует Vehicle
class Car(Vihicle):
    def car_method(self):
        print("Это дочерний метод из класса Car")


# создаём класс Cycle, который наследует Vehicle
class Cycle(Vihicle):
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")


car_a = Car()
car_a.vehicle_method()  # вызов метода родительского класса
car_b = Cycle()
car_b.vehicle_method()  # вызов метода родительского класса


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
