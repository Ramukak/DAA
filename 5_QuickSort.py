def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)

        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
deterministic_quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)


import random

def randomized_partition(arr, low, high):
    random_pivot_index = random.randint(low, high)
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)

        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
randomized_quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)
