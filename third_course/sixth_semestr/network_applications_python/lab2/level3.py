#Задание 1
def max_descending_sequence(arr):
    max_length = 0
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length

arr = [5, 4, 3, 2, 1, 3, 2, 1]
print(max_descending_sequence(arr))

#Задание 2
def move_negatives_to_end(arr):
    non_negatives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
    
    return non_negatives + negatives

arr = [-1, 2, -3, 4, -5, 6]
print(move_negatives_to_end(arr))

#Задание 3
def sort_negatives_descending(arr):
    negatives = sorted([x for x in arr if x < 0], reverse=True)
    neg_idx = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = negatives[neg_idx]
            neg_idx += 1
    
    return arr

arr = [-1, 2, -3, 4, -5, 6]
print(sort_negatives_descending(arr))
