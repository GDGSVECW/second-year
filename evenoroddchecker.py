def check_even_odd(num):
    try:
        if num % 2 == 0: 
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    except TypeError:
        print("Please enter a valid integer.")
