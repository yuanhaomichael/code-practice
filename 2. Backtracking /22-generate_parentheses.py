'''
https://leetcode.com/problems/generate-parentheses/

Intuition:
Build the string until it reaches length 2n, append it to the ans[]
Use backtracking for 2 possible decisions, 
1. to add a left bracket if the amount of left bracket is less than n. 
2. to add a right bracket if the amount of right brackets is less than left bracket

Remember to pop() because in the decision tree, usually try left node first by adding a bracket, then pop it, 
go back the the parent node, then go to the right node trying to append another bracket.
Time: ?
Space: ?
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S=[], left=0, right=0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left<n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right<left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans