import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку значений для x и y
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y = np.linspace(-2 * np.pi, 2 * np.pi, 500)
X, Y = np.meshgrid(x, y)

# Вычисляем значения функции
Z = np.sin(X) * np.cos(Y)

# Построение 3D-графика
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Добавляем цветовую шкалу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
ax.set_title('3D график функции sin(x) * cos(y)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')

plt.show()
