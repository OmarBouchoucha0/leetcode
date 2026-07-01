# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        visited = ""
        res = []

        def removeLast(s: str) -> str:
            print(s)
            while len(s) > 0:
                if s[-1] == ">":
                    s = s[:-2]
                    break
                s = s[:-1]
            return s

        def dfs(root: Optional[TreeNode]):
            nonlocal visited
            nonlocal res
            if root is None:
                return
            if len(visited) == 0:
                visited += str(root.val)
            else:
                visited += "->" + str(root.val)
            if root.left is None and root.right is None:
                res.append(visited)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

            visited = removeLast(visited)

        dfs(root)
        return res
