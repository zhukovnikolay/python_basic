"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from json import dump
from typing import Iterable, List


def my_sum(my_list: Iterable):
    """Суммирует элементы переданного итерируемого объекта"""
    s = 0
    for ind in my_list:
        s += ind
    return s


def my_mean(my_list: List):
    """Функция вычисляет среднее значение элементов переданного списка"""
    return my_sum(my_list) / len(my_list)


companies_dict = {}
companies_profit_dict = {}

with open('task7.txt', 'r', encoding='UTF-8') as user_file, open('task7.json', 'w', encoding='UTF-8') as json_file:
    try:
        for line in user_file:
            company_name = line.split()[0]
            company_profit = int(line.split()[2]) - int(line.split()[3])
            companies_dict[company_name] = company_profit
    except ValueError as e:
        print("В файле присутствуют некорректные данные.\n"
              "Корректный шаблон: 'Название Форма_собственности Выручка(целое число) Издержки(целое число)'\n"
              "Содержание ошибки: ", e)
    except IndexError as e:
        print("В файле присутствуют некорректные данные.\n"
              "Корректный шаблон: 'Название Форма_собственности Выручка(целое число) Издержки(целое число)'\n"
              "Содержание ошибки: ", e)
    try:
        companies_profit_dict['average profit'] = my_mean([profit for profit in companies_dict.values() if profit >= 0])
    except ZeroDivisionError:
        print('В файле нет данных по компаниям')
    dump([companies_dict, companies_profit_dict], json_file)
