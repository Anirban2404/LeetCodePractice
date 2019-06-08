#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:20:14 2019

@author: anirban-mac
"""
"""
939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a 
rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""
from collections import defaultdict

class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cols = defaultdict(list)
        for x, y in points:
            cols[x].append(y)
        print (cols)
        minArea = float('inf')
        prevX = {}
        
        for x in sorted(cols):
            col = cols[x]
            col.sort()
            #print(x, col)
            for j, y2 in enumerate(col):
                for i in range(j):
                    y1 = col[i]
                    print(y1,y2)
                    if (y1, y2) in prevX:
                        print("-->", prevX[y1, y2], x)
                        minArea = min(minArea, (x - prevX[y1, y2]) * (y2 -y1))
                    prevX[y1,y2] = x
                    
        return minArea if minArea < float('inf') else 0
                    
                    
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(Solution().minAreaRect(points))