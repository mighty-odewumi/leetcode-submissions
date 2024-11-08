from collections import Counter

class Solution:
    """
    This is a crude and inefficient solution in terms of space complexity.
    Optimal method would be to use Bit Manipulation which would be later when I learn that.
    """
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)  # Building a Counter uses O(n) time complexity
        # because it has to go through each item given to it. 
        # And Counter and dictionary  in general have a space complexity of O(n) 
        # because they depend on the size of our input.
        # Having a space complexity of O(1) would mean that we use a boolean variable for our solution 

        # for key, value in count.items():
        #     if (value == 1): return key        

        # Another user's Bit Manipulation solution
        # Definitely improved the space complexity
        a = b = 0
        for n in nums:
            b = (b^n)&~a
            a = (a^n)&~b
        return b
