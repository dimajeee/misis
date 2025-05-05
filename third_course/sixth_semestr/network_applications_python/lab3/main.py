# Задание 1
# Написать лямбду, которая удваивает свой аргумент: lambda x: x*2, и использовать её в функции map, чтобы удвоить все элементы в списке.
# print(list(map(lambda x: x ** 2, range(1, 10)))) 


# Задание 2
# Создать лямбда-функцию, которая ищет числа больше нуля: lambda x: x > 0 и использует в filter, чтобы создать список исключительно положительных чисел.
# print(list(filter(lambda x: x > 0, range(-10, 10))))

# Задание 3
# def arithmetic(a, b, operation):
#     operations = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y if y != 0 else "Деление на ноль!"
#     }
#     return operations.get(operation, lambda x, y: "Неизвестная операция")(a, b)

# print(arithmetic(20, 3, '+'))
# print(arithmetic(20, 3, '-'))
# print(arithmetic(20, 3, '*'))
# print(arithmetic(20, 3, '/'))
# print(arithmetic(20, 0, '/'))
# print(arithmetic(20, 3, '^'))



# Задание 4
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе. Использовать методы функционального программирования.
# is_year_leap = lambda year: (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
# print(is_year_leap(2000))
# print(is_year_leap(1900))
# print(is_year_leap(2024))
# print(is_year_leap(2023))

# Задание 5
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (например, с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата. Использовать методы функционального программирования.
# import math

# square = lambda a: (
#     a * 4,
#     a ** 2,
#     a * math.sqrt(2)
# )

# print(square(5))