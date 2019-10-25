#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:40:25 2019

@author: anirban-mac
"""

"""
934. Shortest Bridge
In a given 2D binary array A, there are two islands.  
(An island is a 4-directionally connected group of 1s not connected to any 
other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 
1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that 
the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from collections import deque
class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
       
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(A) or c >= len(A[0]) or A[r][c] == -1:
                return
            if A[r][c] == 1:
                A[r][c] = -1
                for d in directions:
                    i = r + d[0]
                    j = c + d[1]
                    dfs(i, j)
            elif A[r][c] == 0:
                q.appendleft((r, c, 1))
         
        def bfs():
            for r, row in enumerate(A):
                for c, v in enumerate(row):
                    if v == 1:
                        dfs(r, c)
                        return
        bfs()
        
        while q:
            cur_r, cur_c, cur_l = q.popleft()
            for x, y in (cur_r+1, cur_c), (cur_r-1, cur_c), (cur_r, cur_c+1), (cur_r,cur_c-1):
                if 0 <= x < len(A) and 0 <= y < len(A[x]):
                    if A[x][y] == 1:
                        return cur_l
                    elif A[x][y] == 0:
                        A[x][y] = -1
                        q.append((x, y, cur_l+1))
            
            
        
A = [[0,1],[1,0]]
print(Solution().shortestBridge(A))