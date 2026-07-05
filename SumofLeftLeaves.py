# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        curr = {root: "left"}
        sum = 0
        while len(curr) > 0:
            next = {}
            for node in curr:
                if node.left:
                    next[node.left] = "left"
                if node.right:
                    next[node.right] = "right"
                if node.left is None and node.right is None:
                    if curr[node] == "left":
                        sum += node.val
            curr = next
        return sum
