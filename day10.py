def is_palindrome(s):
    return True if s.lower() == s[::-1].lower() else False