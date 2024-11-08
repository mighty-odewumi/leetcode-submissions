from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = {}
        for index, val in enumerate(nums):
            if store.get(val) == 1:
                res = store.get(val)
                res += 1
                store[val] = res
            else:
                store[val] = 1

        # count = Counter(nums)
        
        for key, value in store.items():
            if (value == 1):
                return key