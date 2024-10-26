def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped=False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped=True
        if not swapped:
            break
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected: [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([3, 0, 2, 5, -1, 4, 1]))        # Expected: [-1, 0, 1, 2, 3, 4, 5]
