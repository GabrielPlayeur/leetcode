class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)
    
    def isPowerOfTwo(self, n: int) -> bool:
        Tpow = 1
        while Tpow<=n:
            if Tpow==n: return True
            Tpow*=2
        return False