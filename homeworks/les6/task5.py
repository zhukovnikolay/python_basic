"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

from enum import Enum

# перечисление с типами ручек
class PenType(Enum):
    BALL_PEN = 'Шариковая'
    FOUNTAIN_PEN = 'Перьевая'
    GEL_PEN = 'Гелевая'


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, pen_type: PenType, title='Ручка', color='Синяя'):
        self.title = title
        self.color = color
        self.pen_type = pen_type
        super().__init__(self.title)

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.color.lower()} {self.pen_type.value.lower()} {self.title.lower()}')


class Pencil(Stationery):
    def __init__(self, hardness, title='Карандаш', color='Черный'):
        self.title = title
        self.color = color
        self.hardness = hardness
        super().__init__(self.title)

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.color.lower()} {self.title.lower()} твердостью {self.hardness}')


class Handle(Stationery):
    def __init__(self, title='Маркер', color='Черный'):
        self.title = title
        self.color = color
        super().__init__(self.title)

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.color.lower()} {self.title.lower()}')


pen1 = Pen(PenType.BALL_PEN)
pen2 = Pen(PenType.FOUNTAIN_PEN, color='Черная')
pen1.draw()
pen2.draw()

pencil1 = Pencil('M')
pencil1.draw()

handle1 = Handle()
handle2 = Handle(title='Клевый маркер', color='Желтый')
handle1.draw()
handle2.draw()
