class Solution:
    def climbStairs(self, n: int) -> int:

        a, b, (d, m) = 1, 1, divmod(n,2)

        for _ in range(d):  
            a,b = a+b,a+b+b
            
        return b if m else a