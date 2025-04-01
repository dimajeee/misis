from functools import lru_cache
import math

def calculation(a, b, h, func1, func2, i = 0):
    s = 0
    for x in [x / 10.0 for x in range(int(a * 10), int(b * 10), int(h * 10))]:
        print()
        print(f"y = {func1(x)}")
        s = 0
        i = 0
        while abs(func2(x, i)) > 0.0001:
            tmp = func2(x, i)
            s += tmp
            i += 1
        print(f"s = {s}\ti = {i}")
    return s
 

# @lru_cache()
# def func1_s(x, i):
#     return (-1) ** i * x ** (2 * i) / math.factorial(2 * i)


# def func1_y(x):
#     return math.cos(x)


# calculation(0.1, 1, 0.1, func1_y, func1_s)


# @lru_cache()
# def func3_s(x, i):
#     return  math.cos(i * x) / math.factorial(i)


# def func3_y(x):
#     return math.e ** math.cos(x) * math.cos(math.sin(x))


# calculation(0.1, 1, 0.1, func3_y, func3_s, i=1)


@lru_cache()
def func4_s(x, i):
    return (2 * i + 1) * x ** (2 * i) / math.factorial(i)


def func4_y(x):
    return (1 + 2 * x ** 2) * math.e ** (x ** 2)


calculation(0.1, 1, 0.1, func4_y, func4_s)







