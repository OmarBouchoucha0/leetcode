# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        curr_level = []
        prev_level = [root]
        res = []
        node_vals = []

        while len(prev_level) != 0:
            for node in prev_level:
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)

                node_vals.append(node.val)
            res.append(node_vals)

            prev_level = curr_level
            curr_level = []
            node_vals = []
        return res
