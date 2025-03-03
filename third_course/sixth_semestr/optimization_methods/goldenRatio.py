import math

counter = 0

def find(a, b, e):
    global counter
    x1 = a + (b - a) * ((3 - 5**0.5) / 2)
    x2 = b - (x1 - a)

    while(b - a > e):
        counter+=1

        if(x1 > x2):
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        
    
    x0 = (a + b) / 2
    return x0

def theHalfDivisionMethod(a, b, e):
    global counter
    x1 = (a + b) / 2
    x2 = x1 + e/2

    while(math.abs(b - a) > e):
        counter+=1

        if(x1 > x2):
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        
    
    x0 = (a + b) / 2
    return x0

# Ввод данных
a = float(input("Введите a: "))
b = float(input("Введите b: "))
e = float(input("Введите e: "))

# Нахождение минимума
result = find(a, b, e)

# Вывод результата
print("Минимум функции находится в точке:", result)
print("Итераций - ", counter)
