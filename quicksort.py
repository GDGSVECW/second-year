# QuickSort function to sort an array `a` between indices `low` and `high`
def quicksort(a, low, high):
    # Check if the range is valid (i.e., low is less than or equal to high)
    if low <= high:
        # Partition the array and get the pivot index
        pi = partition(a, low, high)
        # Recursively sort the elements before the pivot
        quicksort(a, low, pi - 1)
        # Recursively sort the elements after the pivot
        quicksort(a, pi + 1, high)

# Partition function to rearrange elements around the pivot
def partition(a, low, high):
    # Set the pivot to the last element in the range
    pivot = a[high]
    # Initialize the index of the smaller element
    i = low - 1
    # Loop through elements from `low` to `high-1`
    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        if a[j] <= pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap the elements at index `i` and `j`
            a[i], a[j] = a[j], a[i]
    # Place the pivot in its correct position
    a[i + 1], a[high] = a[high], a[i + 1]
    # Return the pivot index
    return i + 1

# Input list of integers from the user
a = list(map(int, input().split()))
print("Before Sorting:", a)

# Call quicksort on the entire array
quicksort(a, 0, len(a) - 1)

# Print the sorted array
print("After Sorting:", a)
