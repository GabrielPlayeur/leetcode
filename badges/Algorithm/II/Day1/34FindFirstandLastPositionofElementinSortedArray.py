class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res=[-1,-1]
        if len(nums)==0:
            return res

        res[0]=self.findFirst(nums,target)
        res[1]=self.findLast(nums,target)
        return res

    def findFirst(self,nums,target):
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target and mid-1>-1:
                    return mid
                else:
                    end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return -1
    def findLast(self,nums,target):
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]!=target and mid+1<len(nums):
                    return mid
                else:
                    start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return -1