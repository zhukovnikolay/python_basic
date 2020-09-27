"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
from enum import Enum


# перечисление с направлениями поворота
class Direction(Enum):
    RIGHT = 'направо'
    LEFT = 'налево'


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            print(f'{self.name} поехала со скоростью {self.speed} км/ч')
        else:
            print(f'{self.name} не может ехать нулевой скоростью')

    def stop(self):
        print(f'{self.name} остановилась')
        self.speed = 0

    def turn(self, direction: Direction):
        print(f'{self.name} повернула {direction.value}')
        
    def show_speed(self):
        if self.speed == 0:
            print(f'{self.name} стоит без движения')
        else:
            print(f'{self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)
    
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет со скоростью {self.speed} км/ч. Вы превышаете допустимую (60 км/ч) скорость')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.is_police = False
        super().__init__(speed, color, name, self.is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} едет со скоростью {self.speed} км/ч. Вы превышаете допустимую (40 км/ч) скорость')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.is_police = True
        super().__init__(speed, color, name, self.is_police)


town_car1 = TownCar(0, 'White', 'Kia')
town_car2 = TownCar(70, 'Blue', 'Volkswagen')
town_car1.go()
town_car1.speed = 10
town_car1.go()
town_car1.show_speed()
print(town_car2.is_police)
town_car2.show_speed()

print('#' * 50)

sport_car1 = SportCar(140, 'Red', 'Dodge')
sport_car1.show_speed()
sport_car1.stop()
print(sport_car1.color)
sport_car1.show_speed()

print('#' * 50)

work_car1 = WorkCar(50, 'Orange', 'Kamaz')
work_car2 = WorkCar(10, 'White', 'MAN')
work_car1.show_speed()
work_car2.show_speed()
work_car1.turn(Direction.LEFT)

print('#' * 50)

police_car1 = PoliceCar(50, 'White', 'Ford')
police_car1.go()
print(police_car1.is_police)
police_car1.turn(Direction.RIGHT)
