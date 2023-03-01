class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        currentMax, resMax = 0,0
        for i in range(1,len(prices)):
            currentMax=max(0,currentMax+prices[i]-prices[i-1])
            resMax=max(currentMax,resMax)
        return resMax