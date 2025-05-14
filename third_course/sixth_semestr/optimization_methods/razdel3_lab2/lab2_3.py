from scipy.optimize import linprog
import numpy as np

# Предположим стоимость каждой ВМ (если не указана, возьмем произвольные значения для примера)
# В реальной задаче здесь должны быть фактические стоимости каждого типа ВМ
c = [1, 1.5, 2, 2.5, 0.5]  # Примерные стоимости для F1-F5 соответственно

# Матрица коэффициентов ограничений (Ax ≥ b)
A = [
    [1, 1, 2, 2, 1],        # Виртуальные процессоры
    [1, 2, 4, 5, 1],        # Производительность (ECU)
    [1.7, 3.75, 7.5, 1.7, 0.615],  # Оперативная память
    [160, 410, 820, 350, 0],       # Хранилище
    [2, 3, 3, 3, 1]         # Производительность сети
]

# Вектор ограничений
b = [0.35, 1, 0.256, 2, 2]

# Границы переменных (x ≥ 0)
bounds = [(0, None) for _ in range(5)]

# Решение задачи минимизации
result = linprog(c, A_ub=[-np.array(a) for a in A], b_ub=[-val for val in b], bounds=bounds, method='highs')

# Вывод результатов
if result.success:
    print("Оптимальное решение найдено:")
    types = ['F₁', 'F₂', 'F₃', 'F₄', 'F₅']
    for i, (t, val) in enumerate(zip(types, result.x)):
        print(f"{t} = {val:.4f}")
    print(f"\nМинимальная стоимость = {result.fun:.4f}")
    
    # Проверка ограничений
    print("\nПроверка ограничений:")
    constraints = np.array(A) @ result.x
    for i, (req, actual) in enumerate(zip(b, constraints)):
        print(f"Ограничение {i+1}: Требуется ≥ {req}, Получено {actual:.4f}")
else:
    print("Оптимальное решение не найдено.")
    print("Сообщение:", result.message)