"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from os import path


def is_float(number):
    """Функция проверяет является ли переданное число вещественным"""
    try:
        float(number)
        return True
    except ValueError:
        return False


def my_sum(my_list):
    """Функция суммирует элементы переданного списка"""
    s = 0
    for ind in my_list:
        s += ind
    return s


def my_mean(my_list):
    """Функция вычисляет среднее значение элементов переданного списка"""
    return my_sum(my_list) / len(my_list)


while True:
    user_file_name = input('Введите имя файла для чтения или нажмите Ввод для использования файла по умолчанию...\n')
    if not user_file_name:
        user_file_name = 'task3.txt'
        break
    if path.exists(user_file_name):
        break
    else:
        print(f"Файл с именем '{user_file_name}' отсутствует")

with open(user_file_name, 'r', encoding='UTF-8') as user_file:
    file_content = user_file.readlines()
    employees_stat = []
    for idx, line in enumerate(file_content):
        # Проверяем корректность данных в файле, некорректные строки пропускаем
        if len(line.split()) != 2 or not is_float(line.split()[1]):
            print(f'Строка {idx + 1} содержит некорректные данные и будет пропущена')
            continue
        employees_stat.append([line.split()[0], float(line.split()[1])])
    try:
        print(f"Сотрудники с зарплатой до 20000: {', '.join([name for name, sal in employees_stat if sal < 20000])}\n"
              f"Средняя зарплата: {my_mean([sal for i, sal in employees_stat])}")
    except ZeroDivisionError:
        print(f'Список сотрудников пуст')
