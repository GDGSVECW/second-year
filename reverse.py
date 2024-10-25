def reverse_string(s):
    reversed_str = ""
    for char in s:
        //changed logic of reversing string
        reversed_str = char+reversed_str 
        // returing undeclared variable 
    return reversed_str

# Test the function
print(reverse_string("Hacktoberfest"))  
// argument type incorrect changed
print(reverse_string("12345"))         
print(reverse_string(""))             
