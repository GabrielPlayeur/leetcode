class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low,high = 0,len(nums)-1        
        mid = (low+high)//2
        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]: return mid
            elif target < nums[mid]: low,high = low,mid-1
            else: low,high = mid+1,high
        return -1
    