import numpy as np

def f(x):
    return np.sin(7*x) + 0.5*np.cos(5*x) + 0.3*np.sin(3*x)

def bisection_method_max(a, b, tol):
    while abs(b - a) > tol:
        mid = (a + b) / 2
        if f(mid) > f(mid + tol):
            b = mid
        else:
            a = mid
    return (a + b) / 2

def golden_section_search_min(a, b, tol):
    phi = (1 + np.sqrt(5)) / 2
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    
    return (a + b) / 2

def scan_method(a, b, n, tol):
    h = (b - a) / n
    x = a
    min_x, min_f = x, f(x)
    max_x, max_f = x, f(x)
    extrema_found = False
    
    for i in range(1, n):
        prev_x = x - h
        next_x = x + h
        fx = f(x)
        
        if f(prev_x) >= fx <= f(next_x):  # Минимум
            min_x = golden_section_search_min(prev_x, next_x, tol)
            min_f = f(min_x)
            extrema_found = True
        
        if f(prev_x) <= fx >= f(next_x):  # Максимум
            max_x = bisection_method_max(prev_x, next_x, tol)
            max_f = f(max_x)
            extrema_found = True
        
        x += h
    
    return {"minimum": (min_x, min_f), "maximum": (max_x, max_f), "extrema_found": extrema_found}

if __name__ == "__main__":
    a = float(input("Введите начало отрезка: "))
    b = float(input("Введите конец отрезка: "))
    n = int(input("Введите количество точек разбиения: "))
    tol = float(input("Введите точность: "))
    result = scan_method(a, b, n, tol)
    if result["extrema_found"]:
        print(f"Минимум: x = {result['minimum'][0]:.6f}, f(x) = {result['minimum'][1]:.6f}")
        print(f"Максимум: x = {result['maximum'][0]:.6f}, f(x) = {result['maximum'][1]:.6f}")
    else:
        print("Экстремумы не найдены на данном интервале.")