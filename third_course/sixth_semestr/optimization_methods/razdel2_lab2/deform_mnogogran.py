import numpy as np

def nelder_mead(f, x0, alpha=1.0, gamma=1.5, rho=0.5, sigma=0.5, max_iter=1000, tol=1e-6, bounds=None):
    n = len(x0)
    simplex = [np.array(x0, dtype=float)]
    
    # Инициализация симплекса с ограничениями
    for i in range(n):
        point = np.array(x0, dtype=float)
        point[i] += 0.1  # Уменьшенный шаг для стабильности
        if bounds is not None:
            point[i] = np.clip(point[i], bounds[i][0], bounds[i][1])
        simplex.append(point)
    
    for iteration in range(max_iter):
        # Сортировка вершин по значению функции
        simplex.sort(key=lambda x: f(x))
        
        # Проверка на сходимость
        if np.std([f(x) for x in simplex]) < tol:
            break
            
        centroid = np.mean(simplex[:-1], axis=0)
        
        # Отражение
        xr = centroid + alpha * (centroid - simplex[-1])
        if bounds is not None:
            xr = np.clip(xr, bounds[:, 0], bounds[:, 1])
        fr = f(xr)
        
        if fr < f(simplex[0]):
            # Расширение
            xe = centroid + gamma * (xr - centroid)
            if bounds is not None:
                xe = np.clip(xe, bounds[:, 0], bounds[:, 1])
            if f(xe) < fr:
                simplex[-1] = xe
            else:
                simplex[-1] = xr
        elif fr < f(simplex[-2]):
            simplex[-1] = xr
        else:
            # Сжатие
            if fr < f(simplex[-1]):
                xc = centroid + rho * (xr - centroid)
            else:
                xc = centroid + rho * (simplex[-1] - centroid)
            if bounds is not None:
                xc = np.clip(xc, bounds[:, 0], bounds[:, 1])
            
            if f(xc) < f(simplex[-1]):
                simplex[-1] = xc
            else:
                # Уменьшение
                for i in range(1, len(simplex)):
                    simplex[i] = simplex[0] + sigma * (simplex[i] - simplex[0])
                    if bounds is not None:
                        simplex[i] = np.clip(simplex[i], bounds[:, 0], bounds[:, 1])
    
    best_point = simplex[0]
    best_value = f(best_point)
    return best_point, best_value, iteration + 1

# Тестовые функции
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

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def rosenbrock(x, a=1, b=100):
    return (a - x[0])**2 + b * (x[1] - x[0]**2)**2

# Ограничения для переменных (чтобы избежать переполнений)
bounds_dict = {
    "f": np.array([[-10, 10], [-10, 10], [-10, 10]]),
    "h": np.array([[-10, 10], [-10, 10], [-10, 10]]),
    "z1": np.array([[-5, 5], [-5, 5]]),
    "z2": np.array([[-10, 10], [-10, 10]]),
    "y": np.array([[-5, 5], [-5, 5]]),
    "himmelblau": np.array([[-5, 5], [-5, 5]]),
    "rosenbrock": np.array([[-5, 5], [-5, 5]])
}

# Начальные точки для каждой функции
initial_points = {
    "f": [0, 0, 0],
    "h": [1, 1, 1],
    "z1": [1, 1],
    "z2": [0, 0],
    "y": [1, 1],
    "himmelblau": [4, 4],
    "rosenbrock": [0, 0]
}

# Запуск оптимизации для всех функций
for name, func in zip(["f", "h", "z1", "z2", "y", "himmelblau", "rosenbrock"], [f, h, z1, z2, y, himmelblau, rosenbrock]):
    x0 = initial_points[name]
    bounds = bounds_dict[name]
    result, value, iters = nelder_mead(func, x0, bounds=bounds)
    print(f"Функция {name}:")
    print(f"  Начальная точка: {x0}")
    print(f"  Найден минимум: {np.round(result, 6)}")
    print(f"  Значение функции: {value:.6f}")
    print(f"  Итераций: {iters}\n")


initial_points_rosenbrock = [
    [0, 0],
    [-1, 1],
    [2, -2],
    [-3, -3]
]

print("\nФункция Розенброка (разные начальные точки):")
for x0 in initial_points_rosenbrock:
    result, value, iters = nelder_mead(rosenbrock, x0, bounds=np.array([[-5, 5], [-5, 5]]))
    print(f"  Начальная точка: {x0} → Найден минимум: {np.round(result, 6)}, f = {value:.6f}, итераций: {iters}")