"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class NoEquipmentError(Exception):
    def __init__(self, message):
        self.message = message


class Division:
    divisions = {}

    def __init__(self, div_num, div_name):
        """
        :param div_num: номер подразделения
        :param div_name: наименование подразделения
        """
        self.div_num = div_num
        self.div_name = div_name
        # оборудование в подразделении в формате 'инв.номер: объект'
        self.__equipment = {}
        Division.divisions[self.div_num] = self.div_name

    def transfer_eq_to_storage(self, storage, inv_num):
        """Передает оборудование из подразделения на склад"""
        if inv_num in self.__equipment.keys():
            storage.add_equipment(self.__equipment[inv_num], inv_num)
            self.__equipment.pop(inv_num)
        else:
            raise NoEquipmentError('Оборудование с таким инвентарным номером отсутствует в подразделении')

    def get_eq_from_storage(self, inv_num, equip):
        """Получает оборудование со склада"""
        self.__equipment[inv_num] = equip

    def __str__(self):
        return f'Подразделение {self.div_num} - {self.div_name}'

    @property
    def get_equipment(self):
        return self.__equipment


class Storage:

    def __init__(self, name):
        self.name = name
        # перечень техники на складе в формате 'инв.номер: (объект, (место его хранения на складе))'
        self.__equipment = {}
        # перечень выданных инвентарных номеров
        self.__inventory_numbers = []
        # свободные места хранения на складе
        self.__places_dict = {'Ряд 1': [1, 2, 3], 'Ряд 2': [1, 2, 3]}
        # счетчик оборудования на складе по типам техники
        self.__equipment_count = {}

    def add_equipment(self, equip, inv_num=0):
        """Метод добавляет новое оборудование на склад (если инвентарный = 0) или получает его из подразделения"""
        if not isinstance(inv_num, int):
            raise TypeError('Инвентарный номер должен быть целым положительным числом')
        if not isinstance(equip, Equipment):
            raise TypeError('Оборудование должно быть типа сканер, принтер или копир')
        if not inv_num:
            self.__equipment[self.__inventory_number_gen()] = (equip, self.__place_finder())
            if self.__equipment_count.get(equip.eq_type):
                self.__equipment_count[equip.eq_type] += 1
            else:
                self.__equipment_count[equip.eq_type] = 1
        else:
            self.__equipment[inv_num] = (equip, self.__place_finder())
            self.__equipment_count[equip.eq_type] += 1

    def transfer_equipment(self, inv_num, division: Division):
        """Метод передает оборудование в подразделение"""
        if not isinstance(inv_num, int):
            raise TypeError('Инвентарный номер должен быть целым положительным числом')
        if inv_num in self.__equipment.keys():
            division.get_eq_from_storage(inv_num, self.__equipment[inv_num][0])
            self.__places_dict[self.__equipment[inv_num][1][0]].append(self.__equipment[inv_num][1][1])
            self.__equipment_count[self.__equipment[inv_num][0].eq_type] -= 1
            self.__equipment.pop(inv_num)
        else:
            raise NoEquipmentError('Оборудование с таким инвентарным номером отсутствует на складе')

    @property
    def equipment_count(self):
        """Возвращает количество оборудования на складе всех типов"""
        return self.__equipment_count

    def eq_type_quantity(self, eq_type):
        """Возвращает количество техники на складе по типу оборудования"""
        return self.__equipment_count[eq_type]

    @property
    def free_space(self):
        """Возвращает количество свободного места на складе"""
        space_size = 0
        for val in self.__places_dict.values():
            space_size += len(val)
        return space_size

    @property
    def free_places(self):
        """Возвращает перечень свободных мест на складе"""
        return self.__places_dict

    @property
    def equipment(self):
        """Возвращает полный список оборудования с местами размещения"""
        return self.__equipment

    def __max_space(self):
        """Возвращает ряд, в котором больше всего незанятых мест для равномерного размещения на складе"""
        max_size = 0
        key_max_size = ''
        for key, val in self.__places_dict.items():
            if len(val) > max_size:
                key_max_size = key
                max_size = len(val)
        return str(key_max_size)

    def __inventory_number_gen(self):
        """Генерирует инвентарный номер для новой техники"""
        for i in range(1, 1000):
            if i not in self.__inventory_numbers:
                self.__inventory_numbers.append(i)
                return i
        raise IndexError('Инвентарные номера закончились. Пора заняться списанием техники')

    def __place_finder(self):
        """Возвращает ряд и место, на которых можно разместить оборудования, исходя из равномерности размещения"""
        if self.free_space != 0:
            return self.__max_space(), self.__places_dict[self.__max_space()].pop()
        else:
            raise IndexError('Место на складе закончилось. Пора выдавать технику')


class Equipment:
    def __init__(self, eq_type, vendor, model, prod_year, price):
        self.eq_type = eq_type
        self.vendor = vendor
        self.model = model
        self.prod_year = prod_year
        self.__price = price

    def __str__(self):
        return f'{self.vendor} {self.model}'

    @property
    def get_price(self):
        return self.__price


class Printer(Equipment):
    def __init__(self, vendor, model, prod_year, price, eq_format, is_color):
        self.eq_format = eq_format
        self.is_color = is_color
        super().__init__(eq_type='Printer', vendor=vendor, model=model, prod_year=prod_year, price=price)

    def __str__(self):
        return f'Принтер. Производитель: {self.vendor}, модель: {self.model}'


class Scanner(Equipment):
    def __init__(self, vendor, model, prod_year, price, eq_format, sc_resolution):
        self.eq_format = eq_format
        self.sc_resolution = sc_resolution
        super().__init__(eq_type='Scanner', vendor=vendor, model=model, prod_year=prod_year, price=price)

    def __str__(self):
        return f'Сканер. Производитель: {self.vendor}, модель: {self.model}'


class Copier(Equipment):
    def __init__(self, vendor, model, prod_year, price, copy_speed):
        self.copy_speed = copy_speed
        super().__init__(eq_type='Copier', vendor=vendor, model=model, prod_year=prod_year, price=price)

    def __str__(self):
        return f'Копир. Производитель: {self.vendor}, модель: {self.model}'


if __name__ == '__main__':
    # создаем склад и два подразделения
    storage1 = Storage('Склад 1')
    division1 = Division(1001, 'IT-отдел')
    division2 = Division(1002, 'Юридическая служба')
    print(storage1.free_space)
    # создаем несколько единиц оборудования
    printer1 = Printer('HP', 'LaserJet', 2015, 90000, 'A3', True)
    printer2 = Printer('Epson', 'Photo', 2018, 30000, 'A4', True)
    scanner1 = Scanner('HP', 'ScanJet', 2019, 40000, 'A4', 1200)
    copier1 = Copier('Xerox', 'WorkCentre', 2017, 40000, 60)
    # добавляем его на склад
    try:
        storage1.add_equipment(printer1)
        storage1.add_equipment(printer2)
        storage1.add_equipment(scanner1)
        storage1.add_equipment(copier1)
    except TypeError:
        print('Неверный тип оборудования')
    except IndexError as e:
        print('Произошла ошибка добавления на склад', e)
    print(storage1.equipment)
    print(storage1.eq_type_quantity('Printer'))
    print(storage1.equipment_count)
    # передаем два объекта в подразделение
    try:
        storage1.transfer_equipment(4, division1)
        storage1.transfer_equipment(2, division1)
    except TypeError:
        print('Инвентарный номер введен некорректно')
    except NoEquipmentError:
        print('Оборудование с таким инвентарным номером отсутствует')
    print(storage1.equipment)
    print(storage1.eq_type_quantity('Printer'))
    print(storage1.equipment_count)
    print(division1.get_equipment)
    # возвращаем один из объектов на склад
    try:
        division1.transfer_eq_to_storage(storage1, 2)
    except TypeError:
        print('Инвентарный номер введен некорректно')
    except NoEquipmentError:
        print('Оборудование с таким инвентарным номером отсутствует')
    print(storage1.equipment_count)
    print(division1.get_equipment)
