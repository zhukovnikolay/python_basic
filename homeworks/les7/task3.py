"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, cell_count=1):
        if not isinstance(cell_count, int) or cell_count < 1:
            raise ValueError("Введенное значение количества ячеек некорректно (должно быть целое положительное число)")
        self.cell_count = cell_count

    def __str__(self):
        return f'Количество ячеек в клетке: {self.cell_count}'

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} не является клеткой')
        else:
            return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} не является клеткой')
        elif other.cell_count > self.cell_count:
            raise ArithmeticError('Число ячеек первой клетки не может быть меньше второй')
        else:
            return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} не является клеткой')
        else:
            return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} не является клеткой')
        else:
            return Cell(self.cell_count // other.cell_count)

    def make_order(self, cell_in_row):
        res_list = []
        if self.cell_count // cell_in_row != 0:
            for i in range(self.cell_count // cell_in_row):
                res_list.append(cell_in_row * '*')
            if self.cell_count % cell_in_row != 0:
                res_list.append(self.cell_count % cell_in_row * '*')
        else:
            res_list.append(self.cell_count % cell_in_row * '*')
        return '\n'.join(res_list)


if __name__ == '__main__':
    cell1 = Cell(20)
    cell2 = Cell(3)
    print(f'Первая клетка: {cell1}')
    print(f'Вторая клетка: {cell2}')
    print(f'Клетка после сложения 1 и 2: {cell1 + cell2}')
    print(f'Клетка после вычитания 1 и 2: {cell1 - cell2}')
    print(f'Клетка после умножения 1 и 2: {cell1 * cell2}')
    print(f'Клетка после деления 1 и 2: {cell1 / cell2}')
    print(cell1.make_order(6))
