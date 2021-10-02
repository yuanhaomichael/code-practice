"""
https://leetcode.com/problems/grid-game/
Intuition: 
robot 1's goal is to minimize robot 2's points. 
Robots only move down once because there are only 2 rows. 
So there are n possibilities for robot 1's move, and for each possible
move, robot 2 can either go right first and down at the end, or go 
down first and right. We keep track of for each possible robot 1's path,
the points that robot 2 can gain. 
Time: O(N)
Space: O(1)

Solution: https://leetcode.com/problems/grid-game/discuss/1486340/C%2B%2BJavaPython-Robot1-Minimize-TopSum-and-BottomSum-of-Robot-2-Picture-Explained
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0
        
        for i in range(n):
            topSum -= grid[0][i]
            # why min()? Because robot 1 wants to MINIMIZE robot 2's points
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]
            
        return ans