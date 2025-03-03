# Задание 1
def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Векторы должны быть одинаковой длины")
    
    return sum(a * b for a, b in zip(vector1, vector2))

vector1 = [1, 2, 3, 4]
vector2 = [5, 6, 7, 8]
print(scalar_product(vector1, vector2))

# Задание 2
import math

def vector_length(vector):
    return math.sqrt(sum(x**2 for x in vector))

vector = [1, 2, 3, 4, 5]
print(vector_length(vector))


# Задание 3
def replace_above_average(array):
    average = sum(array) / len(array)
    return [x if x <= average else 0 for x in array]

array = [1, 2, 3, 4, 5, 6, 7]
print(replace_above_average(array))
