import numpy as np
arr = np.random.randint(1, 10, size=10)
print(arr)

def array_multiplier(array):
    s = 1
    for i in range(len(array)):
        s *= array[i]
            
    return(s)
print(array_multiplier(arr))


