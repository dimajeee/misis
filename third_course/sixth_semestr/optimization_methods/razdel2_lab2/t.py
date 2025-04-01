import random

def function(x1, x2):
    # Новая целевая функция
    return 2 * x1**3 - 2 * x1 * x2 + x2**2 

def coordinate_descent(x1, x2, epsilon):
    k = 1
    while True:
        # Определяем случайные шаги h1 и h2
        h1 = random.uniform(-0.1, 0.1)
        h2 = random.uniform(-0.1, 0.1)
        
        # Обновляем координаты
        x1_new = x1 + h1
        x2_new = x2 + h2
        
        # Проверяем критерий остановки
        if abs(function(x1_new, x2_new) - function(x1, x2)) < epsilon:
            break
        
        # Обновляем итерацию и значения
        k += 1
        x1, x2 = x1_new, x2_new
        
    return k, x1, x2

# Пример вызова функции
x1_start, x2_start, epsilon = 1.0, 1.0, 0.001
iterations, x1_opt, x2_opt = coordinate_descent(x1_start, x2_start, epsilon)
print(f"Оптимальные координаты: x1 = {x1_opt}, x2 = {x2_opt} за {iterations} итераций")
