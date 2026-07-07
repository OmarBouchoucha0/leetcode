# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr = [root]
        res = []
        order = "left"
        while len(curr) > 0:
            next = []
            curr_vals = []
            if order == "left":
                for i in range(len(curr)):
                    curr_vals.append(curr[i].val)
                order = "right"
            elif order == "right":
                for i in range(1, len(curr) + 1):
                    curr_vals.append(curr[-i].val)
                order = "left"
            for node in curr:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            curr = next
            res.append(curr_vals)
        return res
