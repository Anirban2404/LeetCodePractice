#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:05:11 2019

@author: anirban-mac
"""

""" 
120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you 
may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = triangle[-1]
        print(memo)
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                memo[j] = triangle[i][j] + min(memo[j], memo[j+1])
            print(memo)
        return memo[0]
            
            
triangle = [[-1],[2,3],[1,-1,-3]]
print(Solution().minimumTotal(triangle))