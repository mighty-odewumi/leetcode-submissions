from collections import Counter

class Solution:
    """
    Get count of each string
    Iterate and get value of letter in ransomNote count
    and save letter picked to global variable
    Get value of letter picked in magazine count
    If value doesn't exist in magazine, return false
    Compare if they are equal.
    If equal, return true, else return false
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Counter(ransomNote)
        magCount = Counter(magazine)
        isRansom = []

        for char in ransomNote:
            # magVal = magCount[char]
            # if magVal == 0: return False
            if ransomCount[char] <= magCount[char]:
                isRansom.append(True)
            else: 
                isRansom.append(False)

        return all(isRansom)
