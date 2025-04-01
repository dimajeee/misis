import numpy as np

def coordinate_descent(f, x0, epsilon=1e-6, max_iter=1000):
    """
    Метод покоординатного спуска для минимизации функции f.
    
    :param f: Функция одной или нескольких переменных
    :param x0: Начальная точка (numpy array)
    :param epsilon: Точность останова
    :param max_iter: Максимальное количество итераций
    :return: Оптимальное значение x и значение функции f(x)
    """
    x = np.array(x0, dtype=float)
    n = len(x)
    k = 0
    
    while k < max_iter:
        x_prev = x.copy()
        
        for i in range(n):
            def func_1d(step):
                x_temp = x.copy()
                x_temp[i] += step
                return f(x_temp)
            
            h_opt = golden_section_search(func_1d, -1, 1, epsilon)
            x[i] += h_opt
        
        if np.abs(f(x) - f(x_prev)) < epsilon:
            break
        
        k += 1
    
    return x, f(x)

def golden_section_search(f, a, b, tol=1e-6):
    """Метод золотого сечения для одномерной оптимизации."""
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return (b + a) / 2

def f(x):
    return -x[0]**2 - x[1]**2 - 10*x[2]**2 + 4*x[2]*x[0] + 3*x[1]*x[2] - 2*x[0] - x[1] + 13*x[2] + 5

def h(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2 - x[2]*x[0] - x[1]

def z1(x):
    return x[0]**3 - x[1]**3 - 2*x[0]*x[1] - 5

def z2(x):
    return x[0]**2 + x[1]**2 - x[0]*x[1] + 5*x[0] + 3*x[1] - 7

def y(x):
    return 2 * x[0]**3 - 2 * x[0] * x[1] + x[1]**2


if __name__ == "__main__":
    x0 = [0, 0, 0]
    
    min_f, val_f = coordinate_descent(f, x0)
    min_h, val_h = coordinate_descent(h, x0)
    min_z1, val_z1 = coordinate_descent(z1, x0)
    min_z2, val_z2 = coordinate_descent(z2, x0)
    min_y, val_y = coordinate_descent(y, x0)
    
    print("Минимум f(x, y, z):", min_f, "Значение в минимуме:", val_f)
    print("Минимум h(x, y, z):", min_h, "Значение в минимуме:", val_h)
    print("Минимум z1(x, y):", min_z1, "Значение в минимуме:", val_z1)
    print("Минимум z2(x, y):", min_z2, "Значение в минимуме:", val_z2)
    print("Минимум y(x1, x2):", min_y, "Значение в минимуме:", val_y)
