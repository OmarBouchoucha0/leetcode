# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = float("inf")

        def dfs(root: Optional[TreeNode], curr_depth):
            nonlocal depth
            if root is None:
                return
            if root.left is None and root.right is None:
                if curr_depth < depth:
                    depth = curr_depth
            dfs(root.left, curr_depth + 1)
            dfs(root.right, curr_depth + 1)

        dfs(root, 1)
        return int(depth)
