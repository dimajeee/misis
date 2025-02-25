import numpy as np

def f(x):
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)

def bisection_method(a, b, tol):
    iterations = 0
    while abs(b - a) > tol:
        iterations += 1
        mid = (a + b) / 2
        if f(mid) < f((a + b) / 2 + tol):
            b = mid
        else:
            a = mid
        print(f"Итерация {iterations}: mid = {mid}, f(mid) = {f(mid)}")
    return (a + b) / 2


def golden_section_search(a, b, tol):
    # Золотое сечение
    phi = (1 + np.sqrt(5)) / 2
    
    # Вычисление точек деления отрезка
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    iterations = 0
    while abs(c - d) > tol:
        iterations += 1
        print(f"Итерация {iterations}: c = {c}, d = {d}, f(c) = {f(c)}, f(d) = {f(d)}")
        if f(c) < f(d):
            b = d
        else:
            a = c
        
        # Пересчет точек деления
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    return (a + b) / 2


def fibonacci_search(a, b, tol):
    # Генерация последовательности Фибоначчи
    fib = [0, 1]
    while fib[-1] < (b - a) / tol:
        fib.append(fib[-1] + fib[-2])
    
    n = len(fib) - 1
    
    # Вычисление точек деления отрезка
    k = n
    while k >= 2:
        x1 = a + fib[k-2] / fib[k] * (b - a)
        x2 = a + fib[k-1] / fib[k] * (b - a)
        
        print(f"Итерация {n-k+1}: x1 = {x1}, x2 = {x2}, f(x1) = {f(x1)}, f(x2) = {f(x2)}")
        
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        k -= 1

    return (a + b) / 2

# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
tol = float(input("Введите точность: "))

min_x = bisection_method(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")

min_x = golden_section_search(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")

min_x = fibonacci_search(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")
