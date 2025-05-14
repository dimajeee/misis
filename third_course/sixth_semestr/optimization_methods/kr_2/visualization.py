import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

def f(x, y):
    return y**4 - 13*y**2 + x**4 - 12*x**2*y

# Создаем сетку для построения графика
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 3D график функции
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X,Y)')
ax.set_title('График функции f(x,y) = y⁴ - 13y² + x⁴ - 12x²y')
fig.colorbar(surf)
plt.show()

# Контурный график
plt.figure(figsize=(10, 8))
contour = plt.contour(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Контурный график функции f(x,y)')
plt.show()