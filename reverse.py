def reverse_string(s):
    reversed_str = ""
    for char in str(s):
        reversed_str = char + reversed_str 
    return reversed_str 

# Test the function
print(reverse_string("Hacktoberfest"))  
print(reverse_string(12345))         
print(reverse_string(""))             
