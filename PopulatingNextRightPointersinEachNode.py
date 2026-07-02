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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return root
        curr = [root]
        while len(curr) > 0:
            next = []
            for i in range(len(curr)):
                if i < len(curr) - 1:
                    curr[i].next = curr[i + 1]
                if curr[i].left or curr[i].right:
                    next.append(curr[i].left)
                    next.append(curr[i].right)
            curr = next
        return root
