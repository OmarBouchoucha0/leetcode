# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        curr = root
        visited = []
        prev = []
        while True:
            if curr.left and curr.left not in visited:
                visited.append(curr.left)
                prev.append(curr)
                curr = curr.left
            elif curr.right and curr.right not in visited:
                visited.append(curr.right)
                prev.append(curr)
                curr = curr.right
            else:
                res.append(curr)
                if len(prev) <= 0:
                    break
                else:
                    curr = visited[-1]
                    prev.pop()
        return res
