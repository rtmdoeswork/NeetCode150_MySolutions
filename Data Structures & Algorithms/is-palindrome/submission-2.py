class Solution:    
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ch for ch in s.lower() if ch.isalnum()])
        w = s[::-1]

        if s == w:
            return True
        else:
            return False