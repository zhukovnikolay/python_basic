"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
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

print([itm for itm in user_args_list if user_args_list.count(itm) == 1])
