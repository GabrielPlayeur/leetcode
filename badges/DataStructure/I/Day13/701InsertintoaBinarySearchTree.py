# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None: return TreeNode(val)
        node,parent=root,None
        while node!=None:
            parent=node
            if node.val<val: node=node.right
            else: node=node.left
        
        if parent.val<val: parent.right=TreeNode(val)
        else: parent.left=TreeNode(val)

        return root