def fibonacci(n):

    if n == 1 or n == 0:

        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases
print(fibonacci(0))  # Expected: 0
print(fibonacci(5))  # Expected: 5
print(fibonacci(10)) # Expected: 55
