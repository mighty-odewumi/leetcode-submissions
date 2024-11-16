class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Use Two pointers at the start and end 
        and then iterate throught the string checking for 
        which value is not equal to the other. 
        If the value of the start pointer is not equal to that of the end, return False.
        At the end of the loop when the start is no more lesser than the end, return True.
        """
        newStr = ""
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        for char in s.lower():
            if char not in alpha.lower():
                continue
            newStr += char

        start = 0
        end = len(newStr) - 1
        # if len(newStr) == 0 or len(newStr) == 1: return True

        while start < end:
            if newStr[start] != newStr[end]:
                return False
            start += 1
            end -= 1
        return True
