"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""


def is_positive_int(number):
    """Проверяет является ли число целым положительным"""
    try:
        if int(number) > 0:
            return True
    except ValueError:
        return False


def fact(n):
    """Вычисляет факториал числа"""
    result = 1
    for number in range(1, n + 1):
        result *= number
        yield result


while True:
    num = input('Введите положительное число, факториал которого необходимо вычислить:\n')
    if is_positive_int(num):
        num = int(num)
        break
    else:
        print('Введено некорректное значение')

for idx, el in enumerate(fact(num)):
    print(f'{idx + 1}! = {el}')
