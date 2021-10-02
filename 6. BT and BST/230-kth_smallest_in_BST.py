#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
Intuition:
inOrder traversal, store in an array, access the kth element.

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        stack = deque()
        
        while True:
            while root:
                stack.appendleft(root)
                root = root.left
            root = stack.popleft()
            k-=1
            if k==0:
                return root.val
            root=root.right
            
        
        
"""
Solution 2: don't really understand
"""
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]        
        
        
        