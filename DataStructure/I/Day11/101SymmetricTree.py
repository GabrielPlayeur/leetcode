# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        rL,rR=root.left,root.right
        stack=[[rL,rR]]
        while len(stack)>0:
            l,r=stack.pop()
            if l==r==None: continue
            elif (l==None or r==None) or (l.val!=r.val): return False
            stack.insert(0, [l.left, r.right])
            stack.insert(0, [l.right, r.left])
        return True
