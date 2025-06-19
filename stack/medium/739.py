class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i,n in enumerate(temperatures):
            while s and s[-1][0] < n:
                v = s.pop()
                res[v[1]] = i - v[1]
            s.append((n,i))
        return res      
