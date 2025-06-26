class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n=sum(set(nums))*2
        for i in nums:
            n-=i
        return n