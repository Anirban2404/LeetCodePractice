#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:13:43 2019

@author: anirban-mac
"""

"""
675. Cut Off Trees for Golf Event

You are asked to cut off trees in a forest for a golf event. The forest is 
represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, 
and this positive number represents the tree's height.
 

You are asked to cut off all the trees in this forest in the order of tree's 
height - always cut off the tree with lowest height first. And after cutting, 
the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps 
you need to walk to cut off all the trees. If you can't cut off all the trees, 
output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least 
one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in 
(0,0) directly without walking.
"""
import collections
import heapq
class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        trees = sorted((v, r, c) for r, row in enumerate(forest) 
                        for c, v in enumerate(row) if v > 1)
        #print(trees)
        sr = sc = ans = 0
        R, C = len(forest), len(forest[0])
        seen = {(sr, sc)}
        def bfs(forest, sr, sc, tr, tc):
            
            queue = collections.deque([(sr, sc, 0)])
            
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc:
                    return d
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or \
                        forest[nr][nc] == 0 or (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
            return -1

        for _, tr, tc in trees:
            d = bfs(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
    
    
    
    def astar(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        heap = [(0, 0, sr, sc)]
        cost = {(sr, sc): 0}
        while heap:
            f, g, r, c = heapq.heappop(heap)
            if r == tr and c == tc: return g
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                    ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                    if ncost < cost.get((nr, nc), 9999):
                        cost[nr, nc] = ncost
                        heapq.heappush(heap, (ncost, g+1, nr, nc))
        return -1
    
forest = [
          [1,2,3],
          [1,0,0],
          [7,6,5]
         ]
print(Solution().cutOffTree(forest))