#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:56:35 2019

@author: anirban-mac
"""

"""
994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten 
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh 
orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never 
rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer 
is just 0.
"""


from collections import deque
class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrows = len(grid)
        ncols = len(grid[0])
        
        queue = deque([])
        count = 0
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        res = 0
        while queue:
            for i in range(len(queue)):
                i, j = queue.popleft()
                
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < nrows and 0 <= y < ncols and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        queue.append((x,y))
            res += 1
        return max(0, res - 1) if count == 0 else -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))