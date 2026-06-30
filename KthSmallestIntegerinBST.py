# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            visited.append(root.val)
            dfs(root.right)

        dfs(root)
        # if you need the kth biggest elemnt yhou can do [-k]
        return visited[k - 1]
