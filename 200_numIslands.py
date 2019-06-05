#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:18:26 2019

@author: anirban-mac
"""

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of 
islands. An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the grid 
are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
import collections
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) <1:
            return 0
        
        count = 0
        nrow = len(grid[0])
        ncol = len(grid)
        
        for i in range(ncol):
            for j in range(nrow):
                if grid [i][j] == "1":
                    #print (i, j)
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs( self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
   
        
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(Solution().numIslands(grid))