class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        s = {}
        for i in range(len(board)):
            for j in range(len(board)):
                n=board[i][j]
                if n==".": continue
                l=f"{n} line {i}"
                r=f"{n} row {j}"
                b=f"{n} boxe {i//3} {j//3}"
                if s.get(l)!=None or s.get(r)!=None or s.get(b)!=None:
                    return False
                s[l],s[r],s[b]=1,1,1
        return True