from collections import Counter

class Solution:
    """
    Get count of each string
    Iterate and get value of letter in ransomNote count
    Get value of letter picked in magazine count
    If total number of letter in ransom map is less than or equal to magazine, 
    Append to list as false
    Else append to list as true
    Finally return whether the list contains totally true or false.
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Counter(ransomNote)
        magCount = Counter(magazine)
        isRansom = set()

        for char in ransomNote:
            if ransomCount[char] <= magCount[char]:
                isRansom.add(True)
            else: 
                isRansom.add(False)

        return all(isRansom)
