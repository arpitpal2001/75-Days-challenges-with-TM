# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if not node:
                return 0
            curr_max = max(curr_max, node.val)
            return (int(curr_max <= node.val) +
                    dfs(node.left, curr_max) + dfs(node.right, curr_max))
        
        return dfs(root, root.val)