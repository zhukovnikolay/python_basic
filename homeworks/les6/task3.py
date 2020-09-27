"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


# Для опроса по вводу нового сотрудника
pos_template = {
    'name': ('Введите имя нового сотрудника:', str),
    'surname': ('Введите фамилию нового сотрудника:', str),
    'position': ('Введите должность нового сотрудника:', str),
    'wage': ('Введите оклад нового сотрудника:', float),
    'bonus': ('Введите премию нового сотруудника:', float)
}

# Заранее подготовленный персонаж
cto = Position(name='Василий', surname='Комаров', position='CTO', wage=350000, bonus=100000)
print(f'У нас уже работает {cto.get_full_name()} в должности {cto.position}')

# Список работников
workers = [cto]
new_enter_flag = True
# Вводим новых сотрудников до отказа пользователя от ввода
while new_enter_flag:
    worker = {}
    for key, value in pos_template.items():
        while True:
            ask = input(f'{value[0]}\n')
            try:
                ask = value[1](ask)
            except ValueError:
                print('Введен некорректный тип данных')
                continue
            worker[key] = ask
            break
    # noinspection PyTypeChecker
    new_worker = Position(name=worker['name'],
                          surname=worker['surname'],
                          position=worker['position'],
                          wage=worker['wage'],
                          bonus=worker['bonus']
                          )
    workers.append(new_worker)

    while True:
        ask_exit = input('Добавить еще одного рабочего? (Да/Нет)\n')
        print(ask_exit)
        if ask_exit.lower() in ('да', 'нет'):
            new_enter_flag = ask_exit == 'да'
            break
        else:
            print("Просто введите 'Да' или 'Нет'")

print('Список работяг:')
for idx, man in enumerate(workers):
    print(f'{idx + 1}. {man.get_full_name()}, {man.position}. Суммарная зарплата: {man.get_total_income()} руб.')
