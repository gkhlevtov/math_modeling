import numpy as np
arr = np.zeros((1, 4))
for (i,j), x in np.ndenumerate(arr):
    print(i,j, sep=' ; ', end='')
    arr[i,j] = float(input('Введите элемент: '))
       
arr = np.append(arr, 0)

print('-----------------')
print('Ваш массив: {}'.format(arr))
print('-----------------')

el = float(input('Введите новый элемент: '))
pos = int(input('Введите позицию от 0 до 4: '))

arr = np.insert(arr, pos, el)
arr = np.delete(arr, -1) 

print('-----------------')
print('Ваш новый массив: {}'.format(arr))
print('-----------------')