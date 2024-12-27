def isPalindrome(self, s: str) -> bool:
    strip_str = ''.join(c.lower() for c in s if c.isalnum())
    return strip_str == strip_str[::-1]