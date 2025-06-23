class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        missing = {}
        for i,n in enumerate(numbers):
            if n in missing:
                return [missing[n], i+1]
            missing[target-n] = i+1
        return []
