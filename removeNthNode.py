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
        llen = 0
        while curr:
            llen += 1
            curr = curr.next
        pos = llen - n
        if pos == 0:
            return head.next
        curr = head
        for _ in range(pos - 1):
            curr = curr.next
        targetnode = curr.next
        curr.next = targetnode.next
        return head
