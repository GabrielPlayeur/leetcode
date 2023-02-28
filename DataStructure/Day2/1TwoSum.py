class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range(len(nums)):
            current = target-nums[i]
            if current in hashmap: return [i,hashmap[current]]
            hashmap[nums[i]] = i
        return -1