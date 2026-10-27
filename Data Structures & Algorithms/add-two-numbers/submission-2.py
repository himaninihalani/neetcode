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
        temp = dummy 
        carry = 0
        while temp1!=None and temp2!=None:
            val1=temp1.val if temp1 else 0
            val2=temp2.val if temp2 else 0
            sumi = val1+val2+carry
            carry = sumi//10
            temp.next = ListNode(sumi%10)
            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1!=None:
            val1=temp1.val if temp1 else 0
            sumi = val1 + carry
            carry = sumi//10
            temp.next = ListNode(sumi%10)
            temp = temp.next
            temp1 = temp1.next
        while temp2!=None:
            val2=temp2.val if temp2 else 0
            sumi = val2+carry
            carry = sumi//10
            temp.next = ListNode(sumi%10)
            temp = temp.next
            temp2 = temp2.next
        if carry>0:
            temp.next = ListNode(carry)
        return dummy.next

        