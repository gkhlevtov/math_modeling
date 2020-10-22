import numpy as np
l = int(input('Введите количество столбцов массива: '))
h = int(input('Введите количество строк массива: '))
arr = np.zeros((h, l))
arr_inv = np.zeros((l, h))
arr_max = np.zeros(l)

for (i,j), x in np.ndenumerate(arr):
    print(i,j, sep=' ; ', end='')
    new_el = float(input('Введите элемент: '))
    arr[i,j] = new_el
    arr_inv[j,i] = new_el

print('---------------------------')
print('Ваш массив:')
print(arr)
print('---------------------------')

for i, x in np.ndenumerate(arr_max):
    arr_max[i] = arr_inv[i].max()
    
print('---------------------------')
print('Максимальные значения столбцов вашего массива: {}'.format(arr_max))
print('---------------------------')