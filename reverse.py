def reverse_string(s):
    if not isinstance(s, str):
        return "Input must be a string."
        
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend the character to reverse
    return reversed_str  # Return the correct variable

# Test the function
print(reverse_string("Hacktoberfest"))  # Should print "tsefrebotkcaH"
print(reverse_string(12345))             # Should print "Input must be a string."
print(reverse_string(""))                 # Should print ""
