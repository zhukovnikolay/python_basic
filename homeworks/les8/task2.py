"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivError(Exception):
    def __init__(self, message):
        self.message = message


def is_float(number: str):
    try:
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        numbers = input("Введите числитель и знаменатель через пробел:\n").split()
        if len(numbers) == 2 and is_float(numbers[0]) and is_float(numbers[1]):
            num, den = float(numbers[0]), float(numbers[1])
            break
        else:
            print('Введены некорректные данные')

    if den == 0:
        raise ZeroDivError("Делить на ноль нельзя")
    print(f'Результат деления: {num / den}')
