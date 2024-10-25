def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str  # Fix the return statement

# Test the function
print(reverse_string("Hacktoberfest"))
print(reverse_string("12345"))  # This should be a string
print(reverse_string(""))  # This will test with an empty string
