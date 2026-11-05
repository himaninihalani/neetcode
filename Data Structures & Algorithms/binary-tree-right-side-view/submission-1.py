# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        result =([])
        ans=[]
        while queue:
            lengq=len(queue)
            current_l=[]
            for _ in range(lengq):
                current =queue.popleft()
                current_l.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(current_l)
            ans.append(current.val)
        return ans

        