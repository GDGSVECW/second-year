def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("Madam"))           
print(is_palindrome("Hello"))            
print(is_palindrome("A man a plan a canal Panama"))  
