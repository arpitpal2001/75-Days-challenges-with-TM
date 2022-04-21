# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root :
            return None
        inorder = []
        self.fill_inorder(root, inorder)
        ans = float("inf")
        for i in range(1, len(inorder)):
            ans = min(ans, abs(inorder[i]-inorder[i-1]))
        return ans
    def fill_inorder(self, root, inorder):
        if not root:
            return
        self.fill_inorder(root.left, inorder)
        inorder.append(root.val)
        self.fill_inorder(root.right, inorder)