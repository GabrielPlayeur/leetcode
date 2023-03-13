# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None: return root
        stack=[root]
        while len(stack)>0:
            node=stack.pop()
            node.left,node.right=node.right,node.left
            if node.left!=None: stack.insert(0,node.left)
            if node.right!=None: stack.insert(0,node.right)
        return root