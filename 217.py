class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
            if cnt[n] > 1:
                return True
        return False
