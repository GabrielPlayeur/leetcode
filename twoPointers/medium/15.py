class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            
            l,r = i+1, len(nums)-1
            while l < r:
                s = n + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
