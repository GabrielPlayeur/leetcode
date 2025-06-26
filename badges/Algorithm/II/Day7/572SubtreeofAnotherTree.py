# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None):
            return False
        if (self.isSame(s, t)): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None and t == None): return True
        if (s == None or t == None): return False

        if (s.val != t.val):
            return False

        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)