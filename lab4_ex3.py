import lab3_ex1 as mm
def mechanical(m, h, v):
    E = ((m * v ** 2) / 2) + m * mm.g * h
    return(E)
print(mechanical(10, 20, 5))