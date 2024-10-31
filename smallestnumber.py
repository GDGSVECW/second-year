def find_smallest(numbers):
    if len(numbers) == 0:
        return None  
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


numbers = [3, 5, 2, 8, 1]
print("The smallest number is:", find_smallest(numbers))
