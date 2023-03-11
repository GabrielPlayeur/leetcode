class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        cur=[0 for _ in range(k)]
        i=0
        while i>=0:
            cur[i]+=1
            if cur[i]>n:
                i-=1
            elif i==k-1:
                res.append(cur.copy())
            else:
                i+=1
                cur[i]=cur[i-1]
        return res