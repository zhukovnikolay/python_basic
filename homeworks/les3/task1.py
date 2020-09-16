"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def my_division(arg1, arg2):
    try:
        result = arg1 / arg2
        print(f'Результат деления: {result}')
    except ZeroDivisionError:
        print("Ошибка деления на 0")


user_arg1 = user_arg2 = 1
while True:
    user_args_list = input("Введите два числа (делимое и делитель) через пробел:\n").split()
    if len(user_args_list) == 2:
        user_arg1, user_arg2 = user_args_list[0], user_args_list[1]
    else:
        print('Вы не ввели два числа')
        continue
    if is_float(user_arg1) and is_float(user_arg2):
        user_arg1 = float(user_arg1)
        user_arg2 = float(user_arg2)
        break
    else:
        print('Введены некорректные значения')

my_division(user_arg1, user_arg2)
