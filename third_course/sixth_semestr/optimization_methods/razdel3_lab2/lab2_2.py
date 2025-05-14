from scipy.optimize import linprog
import numpy as np

# Коэффициенты целевой функции (для минимизации, поэтому знаки меняем)
c = [-4, -5, -6]  # Мы ищем максимум, поэтому меняем знаки для минимизации

# Матрица коэффициентов ограничений-неравенств
A = [
    [1, 2, 3],   # x_A + 2x_B + 3x_C ≤ 35
    [2, 3, 2],    # 2x_A + 3x_B + 2x_C ≤ 45
    [3, 1, 1]     # 3x_A + x_B + x_C ≤ 40
]

# Правые части ограничений
b = [35, 45, 40]

# Границы переменных
x_bounds = (0, None)

# Решение задачи
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds, x_bounds], method='highs')

# Вывод результатов
if result.success:
    print("Оптимальное решение найдено:")
    print(f"x_A = {result.x[0]:.2f}, x_B = {result.x[1]:.2f}, x_C = {result.x[2]:.2f}")
    print(f"Максимальное значение функции F(x) = {-result.fun:.2f}")  # Меняем знак обратно
else:
    print("Оптимальное решение не найдено.")
    print("Сообщение:", result.message)