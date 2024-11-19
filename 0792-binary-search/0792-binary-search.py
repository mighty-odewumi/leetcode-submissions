class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First attempt using an inefficient method.
        # if target in nums: return nums.index(target)
        # else: return -1

        # Efficient Binary Search
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]: 
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]: 
                low = mid + 1
        return -1
