import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку значений для x и y
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
X, Y = np.meshgrid(x, y)

# Функция Гольштейн-Прайс
Z = (1 + (X + Y + 1)**2 * (19 - 14*X + 3*X**2 - 14*Y + 6*X*Y + 3*Y**2)) * \
    (30 + (2*X - 3*Y)**2 * (18 - 32*X + 12*X**2 + 48*Y - 36*X*Y + 27*Y**2))

# Построение 3D-графика
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Добавляем цветовую шкалу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
ax.set_title('3D график функции Гольштейн-Прайс')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')

plt.show()
