#https://leetcode.com/problems/binary-tree-level-order-traversal/
#This is a classic BFS question, storing in a FIFO queue and poping out
#the queue and store nodes of the next level.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q1 = [root]
        result = []
        result.append([root.val])

        #every time you add value to level_result, the nodes are still in the queue and will be popped in the next iteration.
        while q1:
            print(q1)
            level_result = []
            for i in range(len(q1)): 
                node = q1.pop(0)
                if node.left!=None:
                    q1.append(node.left)
                    level_result.append(node.left.val)
                if node.right!=None:
                    q1.append(node.right)
                    level_result.append(node.right.val)
            if len(level_result)!=0: 
                result.append(level_result)

        return result
                