#Задание 1
def get_negative_elements(arr):
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    start = min(min_idx, max_idx)
    end = max(min_idx, max_idx)
    negative_elements = [x for x in arr[start:end+1] if x < 0]
    
    return negative_elements

arr = [-1, 2, -3, 4, -5, 6, -7]
print(get_negative_elements(arr))

#Задание 2
def insert_after_average(arr, p):
    avg = sum(arr) / len(arr)
    closest_idx = min(range(len(arr)), key=lambda i: abs(arr[i] - avg))
    arr.insert(closest_idx + 1, p)
    
    return arr

arr = [1, 2, 3, 4, 5]
p = 10
print(insert_after_average(arr, p))

#Задание 3
def double_after_max(arr):
    max_idx = arr.index(max(arr))
    if max_idx < len(arr) - 1:
        arr[max_idx + 1] *= 2
    
    return arr

arr = [1, 2, 3, 4, 5]
print(double_after_max(arr))
