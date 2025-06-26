class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        minSum=triangle[-1]
        for l in range(n-2,-1,-1):
            for i in range(l+1):
                minSum[i]=min(minSum[i],minSum[i+1])+triangle[l][i]
        return minSum[0]