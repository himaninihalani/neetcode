# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        resu=[]
        self.inorder(root,resu)
        return resu[k-1]
    def inorder(self,node,arr):
        if node:
            self.inorder(node.left,arr)
            arr.append(node.val)
            self.inorder(node.right,arr)
       
    
        
        