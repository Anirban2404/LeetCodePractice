#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:50:09 2019

@author: anirban-mac
"""

"""
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
from collections import defaultdict
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            if node not in seen:
                seen.add(node)
                
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
                    
        graph = defaultdict(list)
        N = len(stones)
        seen = set()
        count = 0
        
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
         
        for i in range(N):
            if i not in seen:
                dfs(i)
                count += 1
        return len(stones) - count if len(stones) > 1 else 0
    
stones = [[0,0]]#,[0,1],[1,0],[1,2],[2,1],[2,2]]
stones =[[0,1],[1,0]]
print(Solution().removeStones(stones))

      