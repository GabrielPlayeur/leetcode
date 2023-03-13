class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return None
        slow,fast=0,0
        while fast < len(nums):
            if nums[fast] != 0: 
                nums[slow], nums[fast] = nums[fast],nums[slow]
                slow+=1
            fast+=1