# Вещество А разлагается на два вещества: Х и У.
# Скорость образования каждого из них пропорциональна количеству неразложившегося вещества.
# Требуется определить закон изменения количеств х и у веществ Х и У в зависимости от времени t при условии,
# что вероятности образования Х и У в единицу времени на единицу массы равны k1 и k2 соответственно.
# Первоначальное количество вещества А задано.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, y = z
    dxdt = k1 * (a - x - y)
    dydt = k2 * (a - x - y)
    return dxdt, dydt

# Определяем начальные значения и параметры
a = 10
k1 = a / 8
k2 = 3 * a / 8

x0 = 0
y0 = 0

z0 = x0, y0

# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)

def solve_func(i, index, key):
    if key == 'point':
        x = t[i]
        y = sol[i, index]
    else:
        x = t[:i]
        y = sol[:i, index]
    return x, y
  

fig, ax = plt.subplots()

ball_line, = plt.plot([], [], '-', color='purple', linewidth = 7)
ball, = plt.plot([], [], 'o', color='purple', linewidth = 10)
ball_line1, = plt.plot([], [], '-', color='orange', linewidth = 7)
ball1, = plt.plot([], [], 'o', color='orange', linewidth = 10)

def animate(i):
    ball.set_data(solve_func(i, 0, 'point'))
    ball_line.set_data(solve_func(i, 0, 'line'))
    ball1.set_data(solve_func(i, 1, 'point'))
    ball_line1.set_data(solve_func(i, 1, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)

plt.grid()
plt.show()