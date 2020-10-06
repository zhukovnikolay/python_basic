"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y}i' if self.y > 0 else f'{self.x} - {abs(self.y)}i'

    def __add__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError('Второе число не является комплексным')
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError('Второе число не является комплексным')
        x_res = (self.x * other.x) - (self.y * other.y)
        y_res = (self.y * other.x) + (self.x * other.y)
        return ComplexNum(x_res, y_res)


if __name__ == '__main__':
    z1 = ComplexNum(2, 4)
    z2 = ComplexNum(2, -2)
    print(f'z1 = {z1}')
    print(f'z2 = {z2}')
    print(f'z1 + z2 = {z1 + z2}')
    print(f'z1 * z2 = {z1 * z2}')
