class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers)-1
        res=[]
        while start<end:
            currentSum = numbers[start]+numbers[end]
            if currentSum == target: return [start+1, end+1]
            elif currentSum < target: start +=1
            else: end -= 1
        return -1