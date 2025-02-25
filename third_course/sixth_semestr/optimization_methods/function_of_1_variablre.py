import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию с множеством экстремумов
def f(x):
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)

# Генерируем значения x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = f(x)

# Строим график
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$f(x) = \sin(7x) + 0.5\cos(5x) + 0.3\sin(3x)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.title("Функция с множеством экстремумов")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()