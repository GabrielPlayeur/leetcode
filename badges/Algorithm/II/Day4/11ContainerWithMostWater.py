from math import inf
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r=0,len(height)-1
        res=-inf
        while l<r:
            cur=(r-l)*min(height[l],height[r])
            if cur>res: res=cur
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res