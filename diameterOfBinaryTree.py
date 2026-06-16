# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = 0
        max_left = 0
        curr = root
        while curr:
            if curr.left is not None:
                curr = curr.left
                left += 1
            else:
                curr = curr.right
                left -= 1
            if left > max_left:
                max_left = left

        right = 0
        max_right = 0
        curr = root
        while curr:
            if curr.right is not None:
                curr = curr.right
                right += 1
            else:
                curr = curr.left
                right -= 1
            if right > max_right:
                max_right = right

        return max_right + max_left
