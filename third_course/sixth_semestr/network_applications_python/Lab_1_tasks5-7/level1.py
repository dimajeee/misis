#Задача 1
def sum_of_squares(p, h):
    return sum((p + i * h) ** 2 for i in range(10))

p = 1 
h = 2  
print(sum_of_squares(p, h))

#Задача 2
def generate_table():
    print("x\t|\ty")
    print("-" * 20)
    for x in [i / 2 for i in range(-8, 9)]:
        y = 0.5 * x ** 2 - 7 * x
        print(f"{x:.1f}\t|\t{y:.4f}")

generate_table()

#Задача 3
import math

def factorial(n):
    return math.factorial(n)

n = 6
print(factorial(n))
