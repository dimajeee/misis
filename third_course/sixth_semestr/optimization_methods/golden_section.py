import numpy as np

def f(x):
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)

def golden_section_search(a, b, tol):
    # Золотое сечение
    phi = (1 + np.sqrt(5)) / 2
    
    # Вычисление точек деления отрезка
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    iterations = 0
    while abs(c - d) > tol:
        iterations += 1
        print(f"Итерация {iterations}: a = {a}, b = {b}, c = {c}, d = {d}, f(c) = {f(c)}, f(d) = {f(d)}")
        if f(c) < f(d):
            b = d
        else:
            a = c
        
        # Пересчет точек деления
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    return (a + b) / 2

# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
tol = float(input("Введите точность: "))

min_x = golden_section_search(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")
