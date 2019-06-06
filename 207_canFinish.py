#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:43:30 2019

@author: anirban-mac
"""
"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it 
possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is 
             possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take 
             course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency 
matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from collections import defaultdict
class Solution:
    white = 1
    gray = 2
    black = 3
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for pair in prerequisites:
            sub, pre = pair
            graph[sub].append(pre)
        
        self.isIndependent = True
        color = {k: self.white for k in range(numCourses)}
        
        def dfs(node):
            if not self.isIndependent:
                return
            color[node] = self.gray
            if node in graph:
                for neighbor in graph[node]:
                    if color == self.white:
                        dfs(neighbor)
                    elif color == self.gray:
                        self.isIndependent = False
            color[node] == self.black
        
        for vertex in range(numCourses):
            if color[vertex] == self.white:
                dfs(vertex)
        #print(self.isIndependent)
        return self.isIndependent
            
            
numCourses = 4
prerequisites = [[1,0],[0,1],[3,1],[3,2]]
print(Solution().canFinish(numCourses, prerequisites))