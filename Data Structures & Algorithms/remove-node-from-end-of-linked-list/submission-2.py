# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        k = 0
        while temp!=None:
            k += 1
            temp = temp.next
        
        
        k = k-n
        if k == 0:
            return head.next
        i = 0
        temp = head
        prev = None 
        while temp!=None and i<=k:
            front = temp.next
            prev = temp
            temp = front 
            i+=1
            if i==k:
                prev.next = prev.next.next
                break
        return head



