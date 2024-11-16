class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        
        for char in s.lower():
            if char not in alpha.lower():
                continue
            newStr += char

        start = 0
        end = len(newStr) - 1
        print(newStr, start, end)
        if len(newStr) == 0 or len(newStr) == 1: return True

        while start < end:
            if newStr[start] != newStr[end]:
                return False
            start += 1
            end -= 1
        return True
