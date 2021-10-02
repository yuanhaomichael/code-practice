
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        arr = []
        def inorder(root, arr):    
            if root.left!=None: 
                inorder(root.left, arr)
            if root!=None:
                arr.append(root.val)
                
            if root.right!=None:
                inorder(root.right, arr)
        
        inorder(root, arr)
        return arr