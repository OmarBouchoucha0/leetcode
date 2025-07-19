# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        seen = set()
        seen.add(head)
        curr = head
        while curr.next:
            if curr.next in seen:
                return True
            seen.add(curr.next)
            curr = curr.next
        return False
