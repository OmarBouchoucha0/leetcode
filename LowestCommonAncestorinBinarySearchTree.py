# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root is None:
            return root
        curr = root
        while curr:
            if (curr.val >= p.val and curr.val <= q.val) or (
                curr.val >= q.val and curr.val <= p.val
            ):
                return curr
            else:
                if curr.val > p.val and curr.val > q.val:
                    curr = curr.left
                if curr.val < p.val and curr.val < q.val:
                    curr = curr.right
        return curr
