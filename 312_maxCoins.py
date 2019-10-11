#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:38:54 2019

@author: anirban-mac
"""

"""
312. Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number 
on it represented by array nums. You are asked to burst all the balloons. If 
the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and 
right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not 
burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for left in range(n-2, -1, -1):
            for right in range(left + 2, n):
                
                   dp[left][right] = max(nums[left] * nums[i] * nums[right]
                   + dp[left][i] + dp[i][right] for i in range(left+1, right))
            
        return dp[0][n-1]
            
            
        
nums = [3,1,5,8]
print(Solution().maxCoins(nums))