def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = reversed_str + char 
    return reversed_string 

print(reverse_string("Hacktoberfest"))  
print(reverse_string(12345))         
print(reverse_string(""))             
