import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import time
from scipy.optimize import minimize

# 1. Определение функции и ее градиента
def f(x, y):
    """Исследуемая функция: f(x,y) = y^4 - 13y^2 + x^4 - 12x^2y"""
    return y**4 - 13*y**2 + x**4 - 12*x**2*y

def grad_f(x, y):
    """Градиент функции"""
    return np.array([4*x**3 - 24*x*y, 4*y**3 - 26*y - 12*x**2])

# 2. Реализация методов оптимизации

def coordinate_descent(f, x0, y0, step=0.1, tol=1e-6, max_iter=1000):
    """Метод покоординатного спуска с постоянным шагом"""
    x, y = x0, y0
    history = {'x': [x], 'y': [y], 'f': [f(x,y)], 'iter': 0, 'time': 0}
    start_time = time.time()
    
    for i in range(max_iter):
        # Поиск по x
        new_x = x + step if f(x+step, y) < f(x,y) else x - step
        if f(new_x, y) < f(x,y):
            x = new_x
        
        # Поиск по y
        new_y = y + step if f(x, y+step) < f(x,y) else y - step
        if f(x, new_y) < f(x,y):
            y = new_y
        
        history['x'].append(x)
        history['y'].append(y)
        history['f'].append(f(x,y))
        
        # Критерий остановки
        if i > 10 and abs(history['f'][-1] - history['f'][-2]) < tol:
            break
    
    history['iter'] = i + 1
    history['time'] = time.time() - start_time
    return x, y, f(x,y), history

def nelder_mead_optimize(f, x0, y0):
    """Метод Нелдера-Мида (используем встроенную реализацию)"""
    start_time = time.time()
    result = minimize(lambda p: f(p[0], p[1]), [x0, y0], method='Nelder-Mead')
    history = {
        'x': [result.x[0]], 
        'y': [result.x[1]], 
        'f': [result.fun],
        'iter': result.nit,
        'time': time.time() - start_time
    }
    return result.x[0], result.x[1], result.fun, history

def conjugate_gradient(f, grad_f, x0, y0, tol=1e-6, max_iter=500):
    """Улучшенный метод сопряженных градиентов"""
    x, y = x0, y0
    history = {'x': [x], 'y': [y], 'f': [f(x,y)], 'iter': 0, 'time': 0}
    start_time = time.time()
    g = grad_f(x, y)
    d = -g
    
    for i in range(max_iter):
        # Проверка на остановку в (0,0)
        if abs(x) < 1e-3 and abs(y) < 1e-3 and i > 10:
            x += np.random.uniform(-1,1)
            y += np.random.uniform(-1,1)
            g = grad_f(x,y)
            d = -g
        
        # Линейный поиск с ограниченным шагом
        alpha = min(0.1, 1.0/(i+1))  # Уменьшаем шаг с итерациями
        for _ in range(100):
            new_x, new_y = x + alpha*d[0], y + alpha*d[1]
            if f(new_x, new_y) < f(x,y) - 0.1*alpha*np.dot(g,g):
                break
            alpha *= 0.8
        
        x_new, y_new = x + alpha*d[0], y + alpha*d[1]
        g_new = grad_f(x_new, y_new)
        
        beta = np.dot(g_new, g_new) / (np.dot(g,g) + 1e-10)
        d = -g_new + beta*d
        
        x, y, g = x_new, y_new, g_new
        history['x'].append(x)
        history['y'].append(y)
        history['f'].append(f(x,y))
        
        if np.linalg.norm(g) < tol:
            break
    
    history['iter'] = i + 1
    history['time'] = time.time() - start_time
    return x, y, f(x,y), history

# 3. Проведение экспериментов
def run_experiments():
    """Запуск всех методов с разными начальными точками"""
    test_points = [(0,0), (3,2), (-3,-2), (1,1), (-1,-1)]
    results = []
    
    for x0, y0 in test_points:
        # Метод покоординатного спуска
        x_cd, y_cd, f_cd, hist_cd = coordinate_descent(f, x0, y0)
        results.append({
            'method': 'Coordinate Descent',
            'x0': x0, 'y0': y0,
            'x': x_cd, 'y': y_cd, 'f': f_cd,
            'iter': hist_cd['iter'], 'time': hist_cd['time']
        })
        
        # Метод Нелдера-Мида
        x_nm, y_nm, f_nm, hist_nm = nelder_mead_optimize(f, x0, y0)
        results.append({
            'method': 'Nelder-Mead',
            'x0': x0, 'y0': y0,
            'x': x_nm, 'y': y_nm, 'f': f_nm,
            'iter': hist_nm['iter'], 'time': hist_nm['time']
        })
        
        # Метод сопряженных градиентов
        x_cg, y_cg, f_cg, hist_cg = conjugate_gradient(f, grad_f, x0, y0)
        results.append({
            'method': 'Conjugate Gradient',
            'x0': x0, 'y0': y0,
            'x': x_cg, 'y': y_cg, 'f': f_cg,
            'iter': hist_cg['iter'], 'time': hist_cg['time']
        })
    
    return results

# 4. Визуализация и вывод результатов
def visualize_and_print_results(results):
    """Визуализация результатов и вывод таблиц"""
    # Создаем график функции
    x = np.linspace(-6, 6, 100)
    y = np.linspace(-6, 6, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    plt.figure(figsize=(12, 8))
    plt.contour(X, Y, Z, levels=np.linspace(-700, 1000, 30), cmap='viridis')
    plt.colorbar(label='Значение функции')
    plt.xlabel('X'); plt.ylabel('Y')
    plt.title('Линии уровня функции f(x,y) с найденными минимумами')
    
    # Добавляем найденные точки
    colors = {'Coordinate Descent': 'red', 'Nelder-Mead': 'green', 'Conjugate Gradient': 'blue'}
    markers = {'Coordinate Descent': 'o', 'Nelder-Mead': 's', 'Conjugate Gradient': '^'}
    
    for res in results:
        plt.scatter(res['x'], res['y'], color=colors[res['method']], 
                   marker=markers[res['method']],
                   label=res['method'], s=100, alpha=0.7)
    
    # Убираем дубликаты в легенде
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    
    plt.grid()
    plt.show()
    
    # Вывод таблицы результатов
    print("\nТаблица результатов оптимизации:")
    table_data = []
    for res in results:
        table_data.append([
            res['method'],
            f"({res['x0']}, {res['y0']})",
            f"({res['x']:.4f}, {res['y']:.4f})",
            f"{res['f']:.4f}",
            res['iter'],
            f"{res['time']:.4f} с"
        ])
    
    print(tabulate(table_data, 
                  headers=['Метод', 'Нач. точка', 'Найденный минимум', 'f(x,y)', 'Итерации', 'Время'],
                  tablefmt='grid'))
    
    # Анализ эффективности
    methods = ['Coordinate Descent', 'Nelder-Mead', 'Conjugate Gradient']
    print("\nСравнительный анализ методов:")
    comp_data = []
    for method in methods:
        method_res = [r for r in results if r['method'] == method]
        avg_iter = np.mean([r['iter'] for r in method_res])
        avg_time = np.mean([r['time'] for r in method_res])
        success_rate = sum(1 for r in method_res if r['f'] < -500)/len(method_res)
        comp_data.append([method, f"{avg_iter:.1f}", f"{avg_time:.4f} с", f"{success_rate:.0%}"])
    
    print(tabulate(comp_data,
                  headers=['Метод', 'Ср. итераций', 'Ср. время', 'Успешность'],
                  tablefmt='grid'))

# 5. Основная программа
if __name__ == "__main__":
    print("Исследование функции f(x,y) = y^4 - 13y^2 + x^4 - 12x^2y")
    print("Сравнение методов оптимизации:\n")
    
    # Запуск экспериментов
    results = run_experiments()
    
    # Визуализация и вывод результатов
    visualize_and_print_results(results)
    
    # Выводы
    print("\nКлючевые выводы:")
    print("1. Функция имеет несколько локальных минимумов:")
    print("   - Глобальные минимумы: (±5.45, 4.95) с f ≈ -600.25")
    print("   - Локальные минимумы: (0, ±2.55) с f ≈ -42.25")
    print("   - Седловая точка: (0,0) с f=0")
    print("\n2. Сравнение методов:")
    print("   - Coordinate Descent: быстрый, но часто находит ближайший локальный минимум")
    print("   - Nelder-Mead: надежный, хорошо находит глобальные минимумы")
    print("   - Conjugate Gradient: точен, но требует аккуратной настройки параметров")
    print("\n3. Рекомендации:")
    print("   - Для надежности использовать комбинацию методов")
    print("   - Начинать с нескольких начальных точек")
    print("   - Визуализировать функцию перед оптимизацией")