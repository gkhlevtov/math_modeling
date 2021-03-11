# Однородная цепь длиной 2.5 м соскальзывает с горизонтального стола, причем в начальный момент времени со стола свисает конец длиной 10 см.
# Пренебрегая трением, найти время соскальзывания всей цепи.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину и количество кадров
frames = 200
t = np.linspace(0, 5, frames)


# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    y, v_y = z
    dydt = v_y
    dv_ydt = y/l * g
    
    return dydt, dv_ydt


# Определяем начальные значения и параметры

m = 0.5
g = 10
l = 2.5
l2 = 0.1

y0 = 0.1
v_y0 = 0
z0 = y0, v_y0

# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)

plt.plot(t, sol[:, 0])

plt.xlim(0, 3)
plt.ylim(0, l)
plt.grid()

plt.show()