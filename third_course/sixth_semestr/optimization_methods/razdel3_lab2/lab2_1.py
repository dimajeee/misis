from scipy.optimize import linprog
import numpy as np

# Коэффициенты целевой функции (для минимизации, поэтому знаки меняем)
c = [-5, -7]  # Мы ищем максимум, поэтому меняем знаки для минимизации

# Матрица коэффициентов ограничений-неравенств
A = [
    [-1, -1],   # x1 + x2 ≥ 5 → -x1 - x2 ≤ -5
    [2, -1],    # 2x1 - x2 ≤ 6
    [-2, 3]     # 2x1 - 3x2 ≥ -18 → -2x1 + 3x2 ≤ 18
]

# Правые части ограничений
b = [-5, 6, 18]

# Границы переменных
x1_bounds = (0, None)
x2_bounds = (0, None)

# Решение задачи
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')

# Вывод результатов
if result.success:
    print("Оптимальное решение найдено:")
    print(f"x1 = {result.x[0]:.2f}, x2 = {result.x[1]:.2f}")
    print(f"Максимальное значение функции L(x) = {-result.fun:.2f}")  # Меняем знак обратно
else:
    print("Оптимальное решение не найдено.")
    print("Сообщение:", result.message)