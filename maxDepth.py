# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1

        def dfs(root: Optional[TreeNode], curr_depth: int):
            nonlocal depth
            if root is None:
                return
            if depth < curr_depth:
                depth = curr_depth
            dfs(root.left, curr_depth + 1)
            dfs(root.right, curr_depth + 1)

        dfs(root, depth)
        return depth
