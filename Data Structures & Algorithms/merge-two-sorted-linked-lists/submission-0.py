# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        dummy = ListNode(0)
        tail = dummy
        while t1 != None and t2 != None:
            if t1.val <= t2.val:
                tail.next = t1
                tail = tail.next
                t1 = t1.next 
            elif t2.val <= t1.val:
                tail.next = t2
                tail = tail.next
                t2 = t2.next
        if t1!=None:
            tail.next = t1
        else:
            tail.next = t2
        return dummy.next      