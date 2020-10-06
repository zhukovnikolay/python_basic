"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    __day = 1
    __month = 1
    __year = 0

    def __init__(self, date: str):
        d, m, y = Date.transform_to_int(date)
        self.check_date(d, m, y)
        self.__day = d
        self.__month = m
        self.__year = y

    @classmethod
    def transform_to_int(cls, date):
        transform_list = []
        if len(date.split('-')) == 3:
            try:
                transform_list = list(map(int, date.split('-')))
            except ValueError:
                print('В строке даты некорректные элементы')
        else:
            raise IndexError('Заданная дата должна быть в формате: дд-мм-гггг')

        return transform_list[0], transform_list[1], transform_list[2]

    @staticmethod
    def check_date(day, month, year):
        correct_date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            correct_date[2] = 29
        if year < 0:
            raise ValueError('Год должен быть больше 0')
        elif month < 1 or month > 12:
            raise ValueError('Месяц должен быть в интервале от 1 до 12')
        elif day < 0 or day > correct_date[month]:
            raise ValueError(f'День должен быть в интервале от 1 до {correct_date[month]}')

    def __str__(self):
        return f'Текущая дата: {self.__day}-{self.__month}-{self.__year}'


new_date = Date('10-11-2005')
print(new_date)

new_date = Date('30-02-2020')
print(new_date)
