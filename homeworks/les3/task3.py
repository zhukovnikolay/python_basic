"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def is_float(number):
    """Проверяет является ли число вещественным"""
    try:
        float(number)
        return True
    except ValueError:
        return False


def two_biggest(*args):
    """Возвращает два самых больших числа из переданных"""
    result = result2 = -float('inf')
    for itm in args:
        if itm > result:
            result2 = result
            result = itm
        elif result2 < itm:
            result2 = itm
    return result, result2


def my_func(arg1, arg2, arg3):
    """Возвращает сумму двух самых больших чисел"""
    return two_biggest(arg1, arg2, arg3)[0] + two_biggest(arg1, arg2, arg3)[1]


user_arg1 = user_arg2 = user_arg3 = 0

# вводим три числа через пробел
while True:
    user_args_list = input("Введите три числа через пробел\n").split()
    # проверяем, что введено три значения
    if len(user_args_list) == 3:
        user_arg1, user_arg2, user_arg3 = user_args_list[0], user_args_list[1], user_args_list[2]
        # если введенные значения - вещественные числа, приводим их к соответствующему типу
        if is_float(user_arg1) and is_float(user_arg2) and is_float(user_arg3):
            user_arg1 = float(user_arg1)
            user_arg2 = float(user_arg2)
            user_arg3 = float(user_arg3)
            break
        # если что-то из введенного не вещественное число, сообщаем об этом
        else:
            print('Введены некорректные значения')
            continue
    # если введено больше или меньше значений, сообщаем об этом
    else:
        print('Вы ввели не три числа')
        continue


print(f'Сумма двух наибольших чисел: {my_func(user_arg1, user_arg2, user_arg3)}')
