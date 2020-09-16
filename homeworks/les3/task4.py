"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_abs(number):
    """Возвращает модуль числа"""
    if number < 0:
        return -number
    else:
        return number


def is_positive_float(number: str):
    """Проверяет является ли число действительным положительным"""
    try:
        if float(number) > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def is_negative_int(number: str):
    """Проверяет является ли число целым отрицательным"""
    if number.startswith('-') and number.count('-') == 1:
        try:
            int(number[1:])
            return True
        except ValueError:
            return False
    else:
        return False


def my_func(x, y):
    """Возводит число x в отрицательную степень y"""
    result = 1
    y = my_abs(y)
    while y:
        result *= x
        y -= 1
    return 1/result


user_arg1 = user_arg2 = 0

# вводим два числа через пробел
while True:
    user_args_list = input("Введите два числа (основание и степень) через пробел\n").split()
    # проверяем, что введен 2 элемента
    if len(user_args_list) == 2:
        user_arg1, user_arg2 = user_args_list[0], user_args_list[1]
        # проверяем, что первый элемент - действительное положительное число, а второй - целое отрицательное
        if is_positive_float(user_arg1) and is_negative_int(user_arg2):
            user_arg1 = float(user_arg1)
            user_arg2 = -float(user_arg2[1:])
            break
        else:
            print('Введены некорректные значения')
            continue
    else:
        print('Вы ввели не два числа')
        continue

print(my_func(user_arg1, user_arg2))
