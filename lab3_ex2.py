import numpy as np
import lab3_ex1 as mm
h = 100
B = 30
a = np.pi / 3
v = np.sqrt((mm.G*h * (np.tan(B)**2)) / (2*(1 - np.tan(B)*np.tan(a))*(np.cos(a))**2))
print(v)

T = 200
e = 300
N = (2 / np.sqrt(np.pi)) * (mm.H / ((mm.k*T) ** (3/2))) * (mm.ei ** -(e / (mm.k*T))) * (e ** (T/2))
print(N)