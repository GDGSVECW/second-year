import re
def is_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]

# Test cases
print(is_palindrome("Madam"))            # Expected: True
print(is_palindrome("Hello"))            # Expected: False
print(is_palindrome("A man a plan a canal Panama"))  # Expected: True
