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

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(A))