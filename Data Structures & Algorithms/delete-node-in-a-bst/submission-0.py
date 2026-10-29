# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(node):
            if not node:
                return 
            current=node
            while current.left:
                current=current.left
            return current

        if root==None:
            return None
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            #case1-no child
            if root.left==None and root.right==None:
                del root
                root = None
            #case2-one child
            elif root.left==None:
                temp=root.right
                root=root.right
                del temp
            elif root.right==None:
                temp=root.left
                root=root.left
                del temp
            #case3-two child
            else:
                temp=findmin(root.right)
                root.val=temp.val
                root.right=self.deleteNode(root.right,temp.val)
        return root
        