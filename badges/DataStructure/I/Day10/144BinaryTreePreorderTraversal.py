# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> int:
        res,stack,node=[],[],root
        while stack or node!=None:
            if node:                
                res.append(node.val)
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                node=node.right
        return res