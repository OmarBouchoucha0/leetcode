# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if not root:
            return 0
        if root.left:
            depth += self.maxDepth(root.left)
        elif root.right:
            depth += self.maxDepth(root.right)
