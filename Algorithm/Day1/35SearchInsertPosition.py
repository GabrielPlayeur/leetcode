class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)-1        
        while low < high:
            mid = low + (high-low)//2
            if target == nums[mid]: return mid
            elif target > nums[mid]: low = mid+1
            else: high = mid
        mid = low + (high-low)//2
        return mid if target <= nums[mid] else mid+1