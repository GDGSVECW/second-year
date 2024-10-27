def is_perfect_number(n):
    if n < 1:
        return False  # Perfect numbers are positive integers
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    return divisors_sum == n

# Test the function
number = int(input("Enter number to check"))
if is_perfect_number(number):
    print(f"{number} is a perfect number!")
else:
    print(f"{number} is not a perfect number.")