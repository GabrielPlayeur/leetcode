class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[]
        for h in range(1,numRows+1):
            res.append([1 if i==0 or i==h-1 else res[h-2][i-1]+res[h-2][i] for i in range(h)])
        return res