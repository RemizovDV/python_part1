'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
class Segment:
    @staticmethod
    def width(A, B):
        return sqrt(sum(tuple(map(lambda a, b: (b - a)**2, A, B))))
class Triangle(Segment):
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C
    def SidesTriangle(self):
        return {'AB': self.width(self._A, self._B),
                'BC': self.width(self._B, self._C),
                'CA': self.width(self._C, self._A)
                }
    def Perimeter(self):
        return (self.SidesTriangle()['AB'] +
                     self.SidesTriangle()['BC'] +
                     self.SidesTriangle()['CA'])

#для вычисления площади треугольника удобно пользоваться формулой Герона
#
    def area(self):
        return ((lambda p, a, b, c:
                      sqrt(p*(p - a)*(p - b)*(p - c)))
                      (self.Perimeter() / 2,
                       self.SidesTriangle()['AB'],
                       self.SidesTriangle()['BC'],
                       self.SidesTriangle()['CA']))
Point1,Point2, Point3 = (0, 0), (0, 3.1), (4.2, 0)
Triangle1 = Triangle(Point1, Point2, Point3)
print('sides of triangle:')
print('\n'.join([str(side) for side in Triangle1.SidesTriangle().values()]))
print('the area of a triangle: {} unit^2'.format(Triangle1.area()))
print('the perimeter of the triangle: {} unit'.format(Triangle1.Perimeter()))