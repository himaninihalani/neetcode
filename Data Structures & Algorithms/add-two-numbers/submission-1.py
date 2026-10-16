# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while temp1 != None and temp2!=None:
            total_sum = temp1.val + temp2.val + carry
            carry = total_sum // 10
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1 != None:
            total_sum = temp1.val + carry
            carry = total_sum // 10
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            temp1 = temp1.next
        while temp2!=None:
            total_sum = temp2.val + carry
            carry = total_sum // 10
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            temp2 = temp2.next
        if carry>0:
            curr.next = ListNode(carry)
        return dummy.next 


        