class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        for n in nums:
            if not cnt.get(n):
                cnt[n] = 1 + cnt.get(n-1, 0) + cnt.get(n+1, 0)
                if cnt.get(n-1): cnt[n-cnt[n-1]] = cnt[n]
                if cnt.get(n+1): cnt[n+cnt[n+1]] = cnt[n]
                res = max(res, cnt[n])
        return res
