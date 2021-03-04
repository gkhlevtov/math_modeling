# Груз массой m = 500 грамм подвешен на пружине и выведен из состояния покоя вытягиванием пружины вниз на ΔL = 8 см.
# При этом возникла сила упругости F0 = 1 Н.
# Затем грузу сообщили скорость, направленную вверх и равную v0 = 0.5 м/с.
# Груз начинает колебаться.
# Смоделируйте движение груза, если:
# а) движение груза происходит без сопротивления,
# б) существует сила сопротивления, равная F = 0.8 m v, направленная противоположно скорости груза,
# в) действует переменная сила f = 5 cos(ω · t) (частоту ω — выбрать произвольным способом).

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 300
t = np.linspace(0, 10, frames)

#a)
"""
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = -k / m * y
    return dxdt, dv_xdt, dydt, dv_ydt

# Определяем начальные значения и параметры

m = 0.5
g = 9.8
F0 = 1
dl = 0.08
v = 10
k = F0 / dl
alpha = 90 * np.pi / 180

x0 = 0
v_x0 = 0
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0
# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 4
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.grid()
plt.show()

"""
#b)
"""
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = -k / m * y - 0.8 * v_y
    return dxdt, dv_xdt, dydt, dv_ydt

# Определяем начальные значения и параметры

m = 0.5
g = 9.8
F0 = 1
dl = 0.08
v = 10
k = F0 / dl
alpha = 90 * np.pi / 180

x0 = 0
v_x0 = 0
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0
# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 4
ax.set_xlim(-edge + 2, edge - 2)
ax.set_ylim(-edge, edge)

plt.grid()
plt.show()
"""
#c)

def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = -k / m * y - 0.8 * v_y
    return dxdt, dv_xdt, dydt, dv_ydt

# Определяем начальные значения и параметры

m = 0.5
g = 9.8
F0 = 1
dl = 0.08
v = 10
k = F0 / dl
alpha = 90 * np.pi / 180

x0 = 0
v_x0 = 0
y0 = 0
v_y0 = v * np.sin(alpha)

z0 = x0, v_x0, y0, v_y0
# Решаем систему диф. уравнений
sol = odeint(move_func, z0, t)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 4
ax.set_xlim(-edge + 2, edge - 2)
ax.set_ylim(-edge, edge)

plt.grid()
plt.show()