#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:17:48 2019

@author: anirban-mac
"""

"""
329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around 
is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is 
not allowed.
"""
class Solution(object):
    directions = {(0,1),(1,0),(0,-1),(-1,0)}
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        memo = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, m, n, i, j, memo))
        return ans
    
    def dfs( self, matrix, m,n, i, j, memo):
        if memo[i][j] != 0:
            return memo[i][j] 
        
        for d in self.directions:
            x = i + d[0]
            y = j + d[1]
            if 0<=x<m and 0<=y<n and matrix[i][j] < matrix[x][y]:
                memo[i][j] = max(memo[i][j] , self.dfs(matrix, m, n, x, y, memo))
        #print("1:", memo, i, j, memo[i][j])
        memo[i][j] += 1
        #print("2:", memo, i, j, memo[i][j])
        return  memo[i][j]
        
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix))