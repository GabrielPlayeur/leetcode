# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        res=[]
        stack=[root]
        while len(stack)>0:
            stackLen = len(stack)
            currentLevel = []
            for _ in range(stackLen):                
                node=stack.pop()
                if node.left: stack.insert(0,node.left)
                if node.right: stack.insert(0,node.right)
                currentLevel.append(node.val)
            res.append(currentLevel)
        return res