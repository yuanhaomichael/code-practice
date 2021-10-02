# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # do a depth first search on the tree, calculate max depth
        # DFS uses a stack
        # traverse down each path, calculate depth
        # time O(N)
        # store the node and its depth as a tuple 
        if root == None:
            return 0
        stack = [(root, 1)]
        max_result = 1
        
        while stack:
            cur = stack.pop()
            if cur[0].right!=None:
                stack.append((cur[0].right, cur[1]+1))
            if cur[0].left!=None:
                stack.append((cur[0].left, cur[1]+1))
                
            # detect leaf
            if cur[0].left==None and cur[0].right==None and cur[1] > max_result:
                max_result = cur[1]
                
        return max_result
            
                
            