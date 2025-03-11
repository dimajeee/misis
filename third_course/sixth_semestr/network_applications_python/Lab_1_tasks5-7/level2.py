#Задача 1
def divide_by_subtraction(n, m):
    quotient = 0
    remainder = n
    
    while remainder >= m:
        remainder -= m
        quotient += 1
    
    return quotient, remainder

n = 17
m = 5
quotient, remainder = divide_by_subtraction(n, m)
print(f"Частное: {quotient}, Остаток: {remainder}")

#Задача 2
import math

def find_time(a, k, target):
    return math.log(target / a, k)

a = 1 
k = 2 
target = 105
time = find_time(a, k, target)
print(f"Время: {time}")

#Задача 3
def calculate_runs(start_distance, increase_rate, days):
    total_distance = 0
    daily_distance = start_distance
    
    for day in range(days):
        total_distance += daily_distance
        daily_distance *= (1 + increase_rate)
    
    return total_distance

def find_days_to_target(start_distance, increase_rate, target_distance):
    total_distance = 0
    daily_distance = start_distance
    days = 0
    
    while total_distance < target_distance:
        total_distance += daily_distance
        daily_distance *= (1 + increase_rate)
        days += 1
    
    return days

def find_days_to_daily_target(start_distance, increase_rate, target_daily_distance):
    daily_distance = start_distance
    days = 0
    
    while daily_distance <= target_daily_distance:
        daily_distance *= (1 + increase_rate)
        days += 1
    
    return days

start_distance = 10 
increase_rate = 0.10 
days = 7

total_distance_7_days = calculate_runs(start_distance, increase_rate, days)
print(f"Суммарный путь за 7 дней: {total_distance_7_days:.2f} км")

days_to_100_km = find_days_to_target(start_distance, increase_rate, 100)
print(f"Дней до 100 км: {days_to_100_km}")

days_to_20_km_daily = find_days_to_daily_target(start_distance, increase_rate, 20)
print(f"Дней до пробега более 20 км в день: {days_to_20_km_daily}")
