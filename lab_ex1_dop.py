a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4 * a * c
print(D)
if D < 0:
    print('Нет действительных корней')
elif D == 0:
    print('x =', (-b)// 2 * a)
else:
    print('x1 =', (-b - D ** (1/2) // (2 * a)))
    print('x2 =', (-b - D ** (1/2) // (2 * a)))