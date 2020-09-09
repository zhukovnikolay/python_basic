"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""
first_int = 0
first_float = 3.541516
first_str = 'My first string!'
print(f"Целое число: {first_int}, вещественное число: {first_float}, строка: '{first_str}'")
first_user_int = input('Введите целое число:\n')
while not first_user_int.isdigit():
    first_user_int = input('Введено некорректное значение. Введите целое число:\n')
else:
    first_user_int = int(first_user_int)
    print('Ваше число:', first_user_int)
first_user_str = input('Введите строку:\n')
second_user_str = input('И ещё одну:\n')
print('Ваши строки:', first_user_str, second_user_str, sep='\n')
