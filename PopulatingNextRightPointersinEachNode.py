"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return root
        curr = [root]
        while len(curr) > 0:
            next = []
            for i, node in enumerate(curr):
                if i < len(curr) - 1:
                    curr[i].next = curr[i + 1]
                else:
                    curr[i].next = None
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            curr = next
        return root
