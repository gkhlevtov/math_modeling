def stepen(a, n):
    b = a
    for i in range(n-1):
        b *= a   
    return(round(b, 7))

print(stepen(3.14, 5))