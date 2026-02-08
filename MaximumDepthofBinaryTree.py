# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        if curr:
            return 0
        depth = 0
        left = self.maxDepth(curr.left)
        right = self.maxDepth(curr.right)
        if left > right:
            depth = left + 1
        else:
            depth = right + 1
        return depth
            
