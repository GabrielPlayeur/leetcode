from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i,j,cur,res=0,0,0,inf

        while (j < len(nums)):
            cur += nums[j]
            j+=1

            while (cur >= target):
                res = min(res, j - i)
                cur -= nums[i]
                i+=1

        return res if res != inf else 0