class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(n, cur, nbOpen):
            if n == 0:
                for _ in range(nbOpen):
                    cur += ")"
                res.append(cur)
                return cur
            gen(n-1, cur+"(", nbOpen+1)
            if nbOpen > 0:
                gen(n, cur+")", nbOpen-1)
        gen(n, "", 0)
        return res
