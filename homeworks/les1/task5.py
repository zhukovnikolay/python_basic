"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


revenue = input('Введите значение выручки компании:\n')
while not is_float(revenue):
    revenue = input('Введено некорректное значение. Введите значение выручки компании:\n')
else:
    revenue = float(revenue)

expenses = input('Введите значение издержек компании:\n')
while not is_float(expenses):
    expenses = input('Введено некорректное значение. Введите значение издержек компании:\n')
else:
    expenses = float(expenses)

earnings = revenue - expenses

if earnings >= 0:
    print(f'Прибыль компании составила: {earnings}. Рентабельность выручки: {round(earnings / revenue * 100, 2)}%')
    employees_num = input('Введите кол-во сотрудников:\n')
    while not employees_num.isdigit():
        employees_num = input('Введено некорректное значение. Введите кол-во сотрудников:\n')
    else:
        employees_num = int(employees_num)
        print(f'Прибыль на одного сотрудника составила: {round(earnings / employees_num, 2)}')
else:
    print(f'Убыток компании составил: {-earnings}')
