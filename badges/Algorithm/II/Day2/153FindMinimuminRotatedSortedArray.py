from math import inf
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1
        minV=inf
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<minV:
                minV=nums[mid]
            if nums[l]<=nums[mid] and nums[r]<nums[l]:
                l=mid+1
            else:
                r=mid-1
        return minV