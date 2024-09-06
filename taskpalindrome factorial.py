def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

strings = ["racecar", "hello", "Noon", "Python"]

for s in strings:
    print(f"'{s}' is a palindrome: {is_palindrome(s)}")
