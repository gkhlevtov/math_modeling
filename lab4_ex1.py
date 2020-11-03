import numpy as np
arr = np.array([1, 2, 3, 5, 7])
def mean_counter(array):
    s = 0
    for i in range(len(array)):
        s += array[i]
        print
        
    m = s/(len(array))    
    return(m)
print(mean_counter(arr))