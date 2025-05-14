# Библиотека SciPy. Что возвращает функция odeint(). Примеры.

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def model(y, t):
    return -y  # dy/dt = -y

y0 = 1.0       # Начальное значение
t = np.linspace(0, 5, 100)  # Временные точки от 0 до 5

# Решение ОДУ
solution = odeint(model, y0, t)

# График решения
plt.plot(t, solution)
plt.xlabel('Время')
plt.ylabel('y(t)')
plt.title('Решение dy/dt = -y')
plt.show()