"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv
from typing import Iterable


def my_map(func, itr: Iterable):
    result = []
    for itm in itr:
        result.append(func(itm))
    return result


def is_float_list(my_list: Iterable):
    for itm in my_list:
        try:
            float(itm)
        except ValueError:
            return False
    return True


def salary_calc(work_hours, rate, prem):
    return work_hours * rate + prem


if len(argv) == 4 and is_float_list(argv[1:4]):
    work_hours_argv, rate_argv, prem_argv = my_map(float, argv[1:4])
    print(f'Заработная плата сотрудника: {salary_calc(work_hours_argv, rate_argv, prem_argv)}')
else:
    print('Введены некорректные значения')
