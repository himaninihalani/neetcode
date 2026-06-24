# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mpp = {}
        temp = head
        while temp != None:
            if temp not in mpp:
                mpp[temp] = 0
            mpp[temp] += 1
            if mpp[temp] == 2:
                return True
            temp = temp.next
        return False
        