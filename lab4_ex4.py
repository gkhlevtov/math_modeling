import numpy as np
def function_counter(a, b, n):
    arr = np.random.randint(a+1, b, size = n)
    arr2 = np.array([])
    y = 1
    for i in range(len(arr)):
        y = (arr[i]) ** 2 - 3
        arr2 = np.append(arr2, y)
            
    return(arr2)
print(function_counter(1,20, 10))

