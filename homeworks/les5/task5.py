"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from typing import Iterable, Callable, List
from random import randint


def is_float_list(my_list: Iterable):
    """Функция проверяет являются ли элементы переданного итерируемого объекта вещественным типом"""
    for itm in my_list:
        try:
            float(itm)
        except ValueError:
            return False
    return True


def my_map(func: Callable, itr: Iterable) -> List:
    """Функция применяет переданную функцию к элементам итерируемого объекта"""
    result = []
    for itm in itr:
        result.append(func(itm))
    return result


def my_sum(my_list: Iterable):
    """Суммирует элементы переданного итерируемого объекта"""
    s = 0
    for ind in my_list:
        s += ind
    return s


with open('task5.txt', 'w') as user_file:
    while True:
        user_str = input(f'Введите числа для записи в файл, разделенные пробелами, или Ввод для автогенерации\n')
        if user_str and not is_float_list(user_str.split()):
            print('Введены некорректные значения.')
        elif not user_str:
            user_str = ' '.join([str(randint(1, 9)) for i in range(randint(3, 7))])
            print(f'Сгенерированный список чисел: {user_str}')
            break
        else:
            break
    user_file.write(user_str)

with open('task5.txt', 'r') as user_file:
    print(f'Сумма чисел в файле: {my_sum(my_map(float, user_file.read().split()))}')
