import numpy as np
import math as m

def f(x):
    return (x ** 2 - 1) * np.e ** np.cos(3 * x) + x
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)
    

def bisection_method_min(a, b, tol):
    iterations = 0
    while abs(b - a) > tol:
        iterations += 1
        mid = (a + b) / 2
        if f(mid) < f((a + b) / 2 + tol):
            b = mid
        else:
            a = mid
        #print(f"Итерация {iterations}: mid = {mid}, f(mid) = {f(mid)}")
    return (a + b) / 2, iterations

def bisection_method_max(a, b, tol):
    iterations = 0
    while abs(b - a) > tol:
        iterations += 1
        mid = (a + b) / 2
        if f(mid) > f((a + b) / 2 + tol):
            b = mid
        else:
            a = mid
        #print(f"Итерация {iterations}: mid = {mid}, f(mid) = {f(mid)}")
    return (a + b) / 2, iterations


def golden_section_search_min(a, b, tol):
    # Золотое сечение
    phi = (1 + np.sqrt(5)) / 2
    
    # Вычисление точек деления отрезка
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    iterations = 0
    while abs(c - d) > tol:
        iterations += 1
        #print(f"Итерация {iterations}: c = {c}, d = {d}, f(c) = {f(c)}, f(d) = {f(d)}")
        if f(c) < f(d):
            b = d
        else:
            a = c
        
        # Пересчет точек деления
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    return (a + b) / 2, iterations

def golden_section_search_max(a, b, tol):
    # Золотое сечение
    phi = (1 + np.sqrt(5)) / 2
    
    # Вычисление точек деления отрезка
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    iterations = 0
    while abs(c - d) > tol:
        iterations += 1
        #print(f"Итерация {iterations}: c = {c}, d = {d}, f(c) = {f(c)}, f(d) = {f(d)}")
        if f(c) > f(d):
            b = d
        else:
            a = c
        
        # Пересчет точек деления
        c = b - (b - a) / phi
        d = a + (b - a) / phi

    return (a + b) / 2, iterations


def fibonacci_search_min(a, b, tol):
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
        
        #print(f"Итерация {n-k+1}: x1 = {x1}, x2 = {x2}, f(x1) = {f(x1)}, f(x2) = {f(x2)}")
        
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        k -= 1
    iteration = n-k+1
    return (a + b) / 2, iteration



def fibonacci_search_max(a, b, tol):
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
        
        #print(f"Итерация {n-k+1}: x1 = {x1}, x2 = {x2}, f(x1) = {f(x1)}, f(x2) = {f(x2)}")
        
        if f(x1) > f(x2):
            b = x2
        else:
            a = x1
        k -= 1
    iteration = n-k+1
    return (a + b) / 2, iteration


def scanning_method(a, b, n):
    # Разбиваем отрезок на n равных частей
    x_values = np.linspace(a, b, n)
    
    # Вычисляем значения функции в точках разбиения
    y_values = f(x_values)
    
    # Находим минимальное значение функции
    min_index = np.argmin(y_values)
    min_x = x_values[min_index]
    min_y = y_values[min_index]
    
    return min_x, min_y


# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
to = input("Введите точность: ")
tol = float(to)
acc = len(str(to)) - 1 

min_x, iteration = bisection_method_min(a, b, tol)
print(f"Минимум функции находится в точке x = {round(min_x, acc)}, Итераций: {iteration}")

min_x, iteration = golden_section_search_min(a, b, tol)
print(f"Минимум функции находится в точке x = {round(min_x, acc)}, Итераций: {iteration}")

min_x, iteration = fibonacci_search_min(a, b, tol)
print(f"Минимум функции находится в точке x = {round(min_x, acc)}, Итераций: {iteration}")

# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
to = input("Введите точность: ")
tol = float(to)
acc = len(str(to)) - 1 

max_x, iteration = bisection_method_max(a, b, tol)
print(f"Максимум функции находится в точке x = {round(max_x, acc)}, Итераций: {iteration}")

max_x, iteration = golden_section_search_max(a, b, tol)
print(f"Максимум функции находится в точке x = {round(max_x, acc)}, Итераций: {iteration}")

max_x, iteration = fibonacci_search_max(a, b, tol)
print(f"Максимум функции находится в точке x = {round(max_x, acc)}, Итераций: {iteration}")

# Пример использования
a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
n = int(input("Введите количество участков разбиения: "))
print("\nМетод сканирования:")
min_x, min_y = scanning_method(a, b, n)
print(f"Минимум функции находится в точке x = {min_x}, f(x) = {min_y}")
