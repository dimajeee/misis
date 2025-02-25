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
        print(f"Итерация {iterations}: a = {a}, b = {b}, mid = {mid}, f(mid) = {f(mid)}")
    return (a + b) / 2

# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
tol = float(input("Введите точность: "))

min_x = bisection_method(a, b, tol)
print(f"Минимум функции находится в точке x = {min_x}")
