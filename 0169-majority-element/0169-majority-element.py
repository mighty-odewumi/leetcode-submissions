from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        lengthOfArr = len(nums)
        majorityConstraint = lengthOfArr / 2

        for key, value in count.items():
            if value > majorityConstraint:
                return key
                