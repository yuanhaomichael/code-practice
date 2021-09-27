"""
Given a 0-indexed integer array nums of size n, find the maximum 
difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # calculate the difference between 0 index and each other index if it's non-negative
        min_ele = nums[0]
        max1 = nums[1] - nums[0]
        
        for i in range(1, len(nums)):
            if max1 < nums[i] - min_ele:
                max1 = nums[i] - min_ele
            
            if nums[i] < min_ele:
                min_ele = nums[i]
        
        if max1 <= 0:
            return -1
        return max1