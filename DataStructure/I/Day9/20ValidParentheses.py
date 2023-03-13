class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        op,cl=['(','[','{'], [')',']','}']
        for c in s:
            if c in op:
                stack.append(c)
            elif c in cl:
                if len(stack)==0: return False
                out=stack.pop()
                if op.index(out)!=cl.index(c): return False
        return len(stack)==0