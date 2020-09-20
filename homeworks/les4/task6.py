"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle
from random import randint
from sys import argv
from time import sleep


def count_func(init_val):
    """Печатает набор значений, начиная с заданного, со случайным ограничением и шагом"""
    end_val = init_val + randint(11, 50)
    count_step = randint(1, 10)
    print(f'Начальное значение: {init_val}, ограничение: {end_val}, шаг: {count_step}')
    for el in count(init_val, count_step):
        if el > end_val:
            break
        else:
            print(el)
            sleep(0.8)


def cycle_func(cycles_num):
    """Печатает сгенерированный список из пяти случайных значений от 1 до 9 заданное количество раз"""
    num = 0
    gen_list = [randint(1, 10) for _ in range(5)]
    print(f'Сгенерированный список для перебора: {gen_list}')
    for el in cycle(gen_list):
        if num == cycles_num * len(gen_list):
            break
        else:
            print(el)
            num += 1
            sleep(0.8)


# ожидается ввод двух аргументов 'cycle кол-во циклов' или 'count начальное значение'
if len(argv) == 3 and argv[2].isdigit():
    script_type, user_value = argv[1], int(argv[2])
    if script_type == 'count':
        count_func(user_value)
    elif script_type == 'cycle':
        cycle_func(user_value)
else:
    print('Некорректные аргументы - введите тип скрипта (cycle или count) и количество циклов или начальное значение')
