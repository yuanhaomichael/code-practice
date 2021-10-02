"""
https://leetcode.com/problems/validate-binary-search-tree/
Intuition 1: inorder traversal while checking
Intuition 2: each node must be within a certain range min and max

Time: O(N)
Space: O(N)


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
            
        return True
        
        
"""
Solution 2
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return True, float('inf'), float('-inf')
            
            # check left & right subtree and also get their min/max
            is_left, left_min, left_max = traverse(node.left)
            is_right, right_min, right_max = traverse(node.right)
            
            # constraints of a valid BST
            are_valid_subtrees = is_left and is_right
            is_value_between = left_max < node.val < right_min
            
            # find min/max value of the subtree  ???
            mmin = min((node.val, left_min, right_min))
            mmax = max((node.val, left_max, right_max))
            
            return are_valid_subtrees and is_value_between, mmin, mmax
        
        return traverse(root)[0]