import time
import random

max_depth = 0

def merge_sort(arr, depth=1):
    global max_depth

    max_depth = max(max_depth, depth)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

sizes = [1000, 5000, 10000]

for size in sizes:
    arr = [random.randint(1, 100000) for _ in range(size)]

    max_depth = 0

    start = time.time()
    merge_sort(arr)
    end = time.time()

    print("\nInput Size:", size)
    print("Execution Time:", round(end - start, 6), "seconds")
    print("Maximum Recursion Depth:", max_depth)
