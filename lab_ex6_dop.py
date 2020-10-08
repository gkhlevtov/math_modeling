y = int(input('Введите год: '))
p = input('до н.э./н.э. ')
if y == 0:
    print('Ошибка!')
elif p == 'н.э.':
    a = 776 + y
    print('OL', (a // 4), end='.')
    print(a % 4 - 1)
else:
    a = 776 - y
    print('OL', (a // 4), end='.')
    print(a % 4)