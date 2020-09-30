"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix_list = matrix_list
        self.check_matrix()

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix_list])

    def __add__(self, other):
        # проверяем, что второй элемент - матрица
        if isinstance(other, Matrix):
            # проверяем, что размеры матриц одинаковы
            if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
                result = [[s_el + ot_el for s_el, ot_el in zip(a, b)] for a, b in zip(self.matrix_list, other.matrix_list)]
                return Matrix(result)
            else:
                raise ValueError('Матрицы не одинакового размера')
        else:
            raise TypeError('Второй элемент не является матрицей')

    def check_matrix(self):
        """Проверяет, матрицу на корректность"""
        if len(self.matrix_list) == 0:
            raise ValueError('Список для создания матрицы пуст')

        if not isinstance(self.matrix_list[0], list):
            raise TypeError('Первый элемент для создания матрицы - не список')

        et_len = len(self.matrix_list[0])

        for line in self.matrix_list:
            if len(line) != et_len:
                raise ValueError('Размерность матрицы некорректна')

        for row in self.matrix_list:
            for el in row:
                if not isinstance(el, int) and not isinstance(el, float):
                    raise TypeError('Матрица содержит элементы некорректного типа')


if __name__ == '__main__':
    matrix1 = Matrix([[2, 1, 3], [1, 2, 4], [2, 3, 4]])
    matrix2 = Matrix([[1, 2, 3], [2, 3, 2], [2, 3, 3]])
    print(f'Матрица 1:\n{matrix1}\n')
    print(f'Матрица 2:\n{matrix2}\n')
    print(f'Их сумма:\n{matrix1 + matrix2}')
