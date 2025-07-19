# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = l1
        prev1 = curr1
        curr2 = l2
        rest = 0
        while curr1 and curr2:
            sum = curr1.val + curr2.val + rest
            if sum >= 10:
                rest = 1
                sum -= 10
            else:
                rest = 0
            curr1.val = sum
            prev1 = curr1
            curr1 = curr1.next
            curr2 = curr2.next
        if curr2:
            print(curr2.val)
            print(prev1.val)
            prev1.next = curr2
            curr1 = prev1.next
        while curr1:
            sum = curr1.val + rest
            if sum >= 10:
                rest = 1
                sum -= 10
            else:
                rest = 0
            curr1.val = sum
            prev1 = curr1
            curr1 = curr1.next
        if rest == 1:
            prev1.next = ListNode(1)
        return l1
