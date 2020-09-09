"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_int = input('Введите целое положительное число:\n')
while not user_int.isdigit():
    user_int = input('Введено некорректное значение. Введите целое положительное число:\n')
else:
    user_int = int(user_int)
max_digit = user_int % 10
user_int //= 10
while user_int:
    if user_int % 10 > max_digit:
        max_digit = user_int % 10
    user_int //= 10
print('Максимальная цифра числа:', max_digit)
