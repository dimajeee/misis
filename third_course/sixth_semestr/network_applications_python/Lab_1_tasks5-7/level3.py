#Задача 1
#Задача 2
#Задача 3

from functools import lru_cache
import math

def calculation(a, b, h, func1, func2, i = 0):
    s = 0
    print("s\t|\ti\t|\ty")
    print("-" * 20)
    for x in [x / 100.0 for x in range(int(a * 100), int(b * 100), int(h * 100))]:
        s = 0
        i = 0
        while abs(func2(x, i)) > 0.0001:
            tmp = func2(x, i)
            s += tmp
            i += 1
        print(f"s = {s:.3f}\t|\ti ={i:.3f}\t|\ty = {func1(x):.3f}")
    return s
 

@lru_cache()
def func4_s(x, i):
    return (2 * i + 1) * x ** (2 * i) / math.factorial(i)


def func4_y(x):
    return (1 + 2 * x ** 2) * math.e ** (x ** 2)

print("Задание 4")
calculation(0.1, 1, 0.1, func4_y, func4_s)

@lru_cache()
def func7_s(x, i):
    return (x ** (2 * i)) / math.factorial(2*i)


def func7_y(x):
    return ((math.e) ** x + math.e ** (-x)) / 2

print("Задание 7")

calculation(0.1, 1, 0.05, func7_y, func7_s)


@lru_cache()
def func8_s(x, i):
    return ((2 * x) ** i) / math.factorial(i)


def func8_y(x):
    return (math.e ** (2 * x))

print("Задание 8")
calculation(0.1, 1, 0.05, func8_y, func8_s)








