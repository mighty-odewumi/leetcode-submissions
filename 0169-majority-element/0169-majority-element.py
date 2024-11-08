from collections import Counter 

class Solution:
    """
    Solved this in O(n) time complexity and O(n) space complexity
    More robust approach would be Moore's voting algorithm, Divide and Conquer 
    using Binary Search, Bit Manipulation
    """
    def majorityElement(self, nums: List[int]) -> int:
        
        # count = Counter(nums)
        # lengthOfArr = len(nums)
        # majorityConstraint = lengthOfArr / 2

        # for key, value in count.items():
        #     if value > majorityConstraint:
        #         return key
        

        # Found an explanation using constant space variables in the Discussions section
        # This uses the Boyer-Moore's algorithm
        result = majorityCounter = 0

        for val in nums:
            if majorityCounter == 0:
                result = val

            if result == val: 
                majorityCounter += 1
            else:
                majorityCounter -= 1
        
        # Having a second pass through the inputs makes sure that we correctly detect if
        # there is really no majority element present
        freqCount = 0
        for value in nums:
            if value == result:
                freqCount += 1
        
        if freqCount > len(nums)/2:
            return result
        else: return -1
        
        # return res
                