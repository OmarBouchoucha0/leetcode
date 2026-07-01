# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        visited = []
        res = []

        def dfs(root: Optional[TreeNode], curr_sum):
            nonlocal visited
            nonlocal res

            if root is None:
                return

            visited.append(root.val)
            curr_sum += root.val
            if root.left is None and root.right is None:
                if curr_sum == targetSum:
                    res.append(visited.copy())

            if root.left:
                dfs(root.left, curr_sum)
            if root.right:
                dfs(root.right, curr_sum)
            visited.pop()

        dfs(root, 0)
        return res
