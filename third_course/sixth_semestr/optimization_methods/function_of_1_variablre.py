import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию с множеством экстремумов
def f(x):
    return (x ** 2 - 1) * np.e ** np.cos(3 * x) + x

# Генерируем значения x
x = np.linspace(-1, 5, 1000)
y = f(x)

# Строим график
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$f(x)$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.title("Функция с множеством экстремумов")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()