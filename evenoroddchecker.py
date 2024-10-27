def check_even_odd(num):
    if num % 2 == 0:  
        print(f"{num} is even")
    else:
        print(num , " is odd") 
    try:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    except TypeError:
        print("Please enter a valid integer.")
check_even_odd(7) 
check_even_odd(-4)  
