import numpy as np
array1 = np.zeros((3, 3))
array2 = np.zeros((3, 3))
array3 = np.zeros((3, 3))


print('Введите значения для массива №1:')

for i, x in np.ndenumerate(array1):
    array1[i] = input()
    
print("Массив №1:")
print(array1)

print('Введите значения для массива №2:')

for i, x in np.ndenumerate(array2):
    array2[i] = input()
    
    if (array1[i] >= array2[i]):
        array3[i] = array1[i]
    else:
        array3[i] = array2[i]
        
print('Массив №2:')
print(array2)

print('Массив №3:')
print(array3)

