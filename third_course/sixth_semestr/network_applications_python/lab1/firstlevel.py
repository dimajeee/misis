#10.	Возвести число 3 в 7-ю степень, не используя операцию возведения в степень.
# x = input("Введите число которое нужно возвести в степень 3 и 7: ")
# print(int(x) ** 3, int(x) ** 7)


# 11.	Напечатать заданную последовательность чисел:
# а) 1 2 3 4 5 6, 
# б) 5 5 5 5 5 5.
# print((" ".join([str(i) for i in range(1, 7)])))
# print("5 " * 6)


# 8.	Вычислить s = 1! + 2! + ... + 6!
def getfact(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

print(sum([getfact(x) for x in range(1, 7, 1)]))
