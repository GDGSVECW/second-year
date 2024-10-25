def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test cases
print(is_palindrome("Madam"))            # Expected: True
print(is_palindrome("Hello"))            # Expected: False
print(is_palindrome("A man a plan a canal Panama"))  # Expected: True
