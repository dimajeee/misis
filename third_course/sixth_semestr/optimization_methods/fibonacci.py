import numpy as np

def f(x):
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)

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
        
        print(f"Итерация {n-k+1}: a = {a}, b = {b}, x1 = {x1}, x2 = {x2}, f(x1) = {f(x1)}, f(x2) = {f(x2)}")
        
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

min_x = fibonacci_search(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")
