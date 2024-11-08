from collections import Counter 

class Solution:
    """
    Solved this in O(n) time complexity and O(n) space complexity
    More robust approach would be Moore's voting algorithm, Divide and Conquer using Binary Search,
    Bit Manipulation
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        lengthOfArr = len(nums)
        majorityConstraint = lengthOfArr / 2

        for key, value in count.items():
            if value > majorityConstraint:
                return key
                