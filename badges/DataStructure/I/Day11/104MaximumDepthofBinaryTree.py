# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.dfs(root.left, 2), self.dfs(root.right, 2))

    def dfs(self, node, deep):
        if node==None: return deep-1
        return max(self.dfs(node.left,deep+1),self.dfs(node.right,deep+1))
