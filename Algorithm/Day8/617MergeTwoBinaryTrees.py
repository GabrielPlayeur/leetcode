# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1==None or root2==None: return root1 if root2==None else root2
        root1.val += root2.val
        if root2.left != None:
            if root1.left != None: #go sum left nodes
                root1.left = self.mergeTrees(root1.left, root2.left)
            else: #root 1 haven't left node juste merge
                root1.left = root2.left         
        if root2.right != None:
            if root1.right != None: #go sum right nodes                
                root1.right = self.mergeTrees(root1.right, root2.right)
            else: #root 1 haven't right node juste merge
                root1.right = root2.right
        return root1