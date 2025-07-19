# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        curr1 = list1
        curr2 = list2
        head = ListNode()
        if curr1.val > curr2.val:
            head.val = curr2.val
            curr2 = curr2.next
        else:
            head.val = curr1.val
            curr1 = curr1.next
        curr = head
        while curr1 and curr2:
            newList = ListNode()
            if curr1.val > curr2.val:
                newList.val = curr2.val
                curr2 = curr2.next
            else:
                newList.val = curr1.val
                curr1 = curr1.next
            curr.next = newList
            curr = curr.next
        while curr1:
            newList = ListNode()
            newList.val = curr1.val
            curr1 = curr1.next
            curr.next = newList
            curr = curr.next
        while curr2:
            newList = ListNode()
            newList.val = curr2.val
            curr2 = curr2.next
            curr.next = newList
            curr = curr.next
        return head
