# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans=[]
        self.inorder(root,ans)
        for i in range(1,len(ans)):
            if ans[i]<=ans[i-1]:
                return False
        return True

    def inorder(self,node,result):
        if node:
            self.inorder(node.left,result)
            result.append(node.val)
            self.inorder(node.right,result)
        return result