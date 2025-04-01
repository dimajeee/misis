import math

# 8.	Вкладчик положил в банк 10 000 рублей под 8 % в месяц. Определить, через какое время сумма удвоится. 
startMoney = 10000
x = startMoney
count = 0
while x < startMoney * 2:
    x *= 1.08
    count += 1
print(count)


# 2.	Определить наибольшее значение сомножителя n, для которого произведение р = 1 · 4 · 7 ·...· n не превышает L = 30 000.
def getadd3fact(x):
    fact = 1
    for i in range(1, x + 1, 3):
        fact *= i
    return fact

n = 1
while getadd3fact(n) < 30000:
    n += 1 
print(n)



# 1.	Вычислить сумму s = cos x + (cos 2x)/22 + ... + (cos nx)/n2 +.... Суммирование прекратить, когда очередной член суммы по модулю будет меньше ε = 0,0001.
def getcosfunc(x):
    return math.cos(2 * x)/(x ** 2)


s = 0
for n in range(1, 100):
    x = getcosfunc(n)
    s += x
    if abs(x) < 0.0001:
        print(n)
        break