def check_even_odd(num):
    if num % 2 == 0:  
        print(f"{num} is even")
    else:  # Added colon here
        print(f"{num} is odd")  # Changed to f-string for consistency
    return None

# Test the function
check_even_odd(7) 
check_even_odd(-4)
