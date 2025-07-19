# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        step = curr
        for _ in range(n):
            step = step.next
        if not step:
            return head.next
        while step.next:
            curr = curr.next
            step = step.next
        curr.next = curr.next.next
        return head
