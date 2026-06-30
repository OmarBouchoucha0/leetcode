# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxi = float("inf")
        mini = float("-inf")

        def dfs(root: Optional[treeNode], maxi: int, mini: int):
            if root is None:
                return True
            if maxi > root.val > mini:
                return dfs(root.right, maxi, root.val) and dfs(
                    root.left, root.val, mini
                )
            return False

        return dfs(root, maxi, mini)
