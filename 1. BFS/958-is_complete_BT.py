# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
To check completeness, 
Case 1: if a node has left child none and right child not none, there is 
a bubble in the tree, and it's not complete.
Case 2: if we see a node with a missing child, and then we see another node 
with valid children, then the tree is not complete. 

Time: O(n)
Space: O(n)

Solution 2: no node should come after a null, so basically do a level order
traversal and check if any node comes after null.
Use python Deque to use as a queue because pop(0) is itself O(n)
"""
class Solution:
    def isCompleteTree(self, root) -> bool:
        q = [root]
        # flag to mark if we've seen a node with at least 1 missing child
        flag = False
        while q:
            n = q.pop(0)
            # Case 2: if we've already seen a node with a missing child, 
            # and the current node has valid children, then return False
            if flag == True and n!=None and (n.left!= None or n.right!=None):
                return False

            # Case 1: 
            if n!=None and n.left==None and n.right!=None:
                return False
            
            # BFS actions
            if n!=None:
                q.append(n.left)
                q.append(n.right)
            
            # if there's a node with at least 1 missing child
            if n!=None and (n.left==None or n.right==None):
                flag = True
                
                
        return True
             
                
            
                
            
        
        