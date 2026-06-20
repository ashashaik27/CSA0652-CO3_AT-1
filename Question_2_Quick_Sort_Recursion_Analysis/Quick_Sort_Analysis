import random
import time
max_depth = 0
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high, depth=1):
    global max_depth
    while low < high:
        max_depth = max(max_depth, depth)
        pi = partition(arr, low, high)
        if (pi - low) < (high - pi):
            quick_sort(arr, low, pi - 1, depth + 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high, depth + 1)
            high = pi - 1
sizes = [1000, 5000, 10000]
for size in sizes:
    arr = [random.randint(1, 100000) for _ in range(size)]
    max_depth = 0

    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    print("\nInput Size:", size)
    print("Execution Time:", round(end - start, 6), "seconds")
    print("Maximum Recursion Depth:", max_depth)
