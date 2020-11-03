def fib(n):
    fib_lst = []

    i = 0
    c = 0
    b = 1
    d = 0
    while i < n:
        fib_lst.append(d)
        d = b + c
        b = c
        c = d
        i += 1
    return (fib_lst[-1])

print(fib(7))
