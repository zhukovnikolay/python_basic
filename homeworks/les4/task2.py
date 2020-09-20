"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from typing import Iterable


def is_float_list(my_list: Iterable):
    """Проверяет элементы переданного итерируемого объекта на соответствуию вещественному типу"""
    for itm in my_list:
        try:
            float(itm)
        except ValueError:
            return False
    return True


def my_map(func, itr: Iterable):
    """Применяет функцию к элементам итерируемого объекта"""
    result = []
    for itm in itr:
        result.append(func(itm))
    return result


while True:
    user_args_list = input("Введите список чисел через пробел:\n").split()
    if is_float_list(user_args_list):
        user_args_list = my_map(float, user_args_list)
        break
    else:
        print('Введены некорректные значения')
        continue

print([itm for num, itm in enumerate(user_args_list) if itm > user_args_list[num - 1] and num != 0])
