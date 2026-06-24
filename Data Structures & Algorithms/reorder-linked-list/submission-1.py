# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return head
        temp = head
        sta = []
        while temp!=None:
            sta.append(temp)
            temp = temp.next
        total = len(sta)//2
        limit  = len(sta) - total
        temp = head
        while temp!=None and len(sta)>limit:
            front = temp.next
            add = sta.pop()
            temp.next = add
            add.next = front
            temp = front
        if temp:
            temp.next = None
        