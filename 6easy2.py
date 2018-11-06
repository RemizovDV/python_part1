'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt
class Trapeze:
    def __init__(self, a, b, c, d):
        try:
            self.AB = sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
            self.BC = sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2)
            self.CD = sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2)
            self.DA = sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2)
            
        except TypeError:
            print('Параметры заданы неверно')
            
    def printr(self):
        print('стороны')
        print(self.AB)
        print(self.BC)
        print(self.CD)
        print(self.DA)
        
    def CheckTr(self):
        return self.AB == self.CD
    def Perimeter(self):
        return (self.AB + self.BC + self.CD + self.DA)
    def area(self):
        if self.CheckTr():
            h = sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            return (1/2 * (self.BC + self.DA) * h)
        else:
            p = self.Perimeter() / 2
            return (self.BC + self.DA)/abs(self.DA - self.BC)*sqrt((p-self.DA)*(p-self.BC)*(p-self.DA-self.AB)*(p-self.DA-self.CD))
Trapeze1 = Trapeze((0, 0), (0, 1), (5, 1), (5, 0))
Trapeze1.printr()
print('Трапеция с AD и BC\nявляется равнобокой: {0}\n'
      'с Площадь {1} и  Периметр {2} '
      ' '.format(Trapeze1.CheckTr(), Trapeze1.area(), Trapeze1.Perimeter()))
