def check_even_odd(num):
    try:
        if num % 2 == 0:
            print(f"{num} is even")
        # If not even, then it's odd
        else:
            print(f"{num} is odd")
    except TypeError:
        print("Please enter a valid integer.")
check_even_odd(7) 
check_even_odd(-4)  
