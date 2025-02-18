import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку значений для x и y
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

# Функция Химмельблау
Z = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2

# Построение 3D-графика
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Добавляем цветовую шкалу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
ax.set_title('3D график функции Химмельблау')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')

plt.show()
