class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First attempt using an inefficient method.
        """
        if target in nums: return nums.index(target)
        else: return -1
        """

        # Efficient Binary Search
        low = 0
        high = len(nums) - 1

        # Iterative method
        """
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]: 
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]: 
                low = mid + 1
        return -1
        """

        # Recursive Method
        def binarySearch(nums, low, high):

            mid = (low + high) // 2
            if high < low: return -1

            if target == nums[mid]: return mid
            elif target > nums[mid]: return binarySearch(nums, mid + 1, high)
            elif target < nums[mid]: return binarySearch(nums, low, mid - 1)

        return binarySearch(nums, low, high)
