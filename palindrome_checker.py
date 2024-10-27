def is_palindrome(s):
    # Remove any spaces and convert to lowercase to ensure accurate comparison
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
string = input()
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")