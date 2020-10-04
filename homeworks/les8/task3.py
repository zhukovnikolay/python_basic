"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
"""


class CheckNumbersError(Exception):
    def __init__(self, message='Введено не число'):
        self.message = message


class Numbers:
    def __init__(self, number):
        self.number = number
        self.check_number()

    def check_number(self):
        try:
            float(self.number)
        except ValueError:
            raise CheckNumbersError()


if __name__ == '__main__':
    user_list = []
    while True:
        el = input("Вводите числа, для окончания ввода введите 'stop':\n")
        if el == 'stop':
            break
        try:
            new_el = Numbers(el)
            user_list.append(float(el))
        except CheckNumbersError:
            print('Элемент не будет добавлен, т.к. не является числом')
    print(f"Список элементов: {user_list}")
