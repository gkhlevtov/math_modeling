import numpy as np
import lab3_ex1 as mm
def Square(Type, a, b, c, r):
    if Type == 'Прямоугольник' or Type == 'прямоугольник':
        S = a * b
        return S
    elif Type == 'Треугольник' or Type == 'треугольник':
        p = (a+b+c) / 2
        S = np.sqrt(p * (p-a) * (p-b) * (p-c))
        return S
    elif Type == 'круг' or Type == 'Круг':
        S = mm.pi * (r ** 2)
        return S
    else:
        return False
    
print(Square(Type='треугольник', a = 17, b = 30, c = 17, r = 0))
print(Square(Type='Прямоугольник', a = 12, b = 5, c = 0, r = 0))
print(Square(Type='Круг', r = 4, a = 0, b = 0, c = 0))
print(Square(Type = 'kvadratt', r =3, a =55, c= 2, b=1))