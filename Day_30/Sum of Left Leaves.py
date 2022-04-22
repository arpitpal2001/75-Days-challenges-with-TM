# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        res = 0
        while len(stack)>0: 
            curr = stack.pop(0)
            if curr is not None:
                if curr.left is not None:
                    if curr.left.left is None and curr.left.right is None:
                        res += curr.left.val
                stack.insert(0, curr.right)
                stack.insert(0, curr.left)
        return res