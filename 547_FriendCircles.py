#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:23:28 2019

@author: anirban-mac
"""

"""
547. 547. Friend Circles
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend 
of B, and B is a direct friend of C, then A is an indirect friend of C. And we 
defined a friend circle is a group of students who are direct or indirect 
friends.

Given a N*N matrix M representing the friend relationship between students in 
the class. If M[i][j] = 1, then the ith and jth students are direct friends 
with each other, otherwise not. And you have to output the total number of 
friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a 
friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd 
students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same 
friend circle, so return 1.

"""

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        nrows = len(M)
        ncols = len(M[0])
        
        visited = [0 for _ in range(nrows)]
        count = 0
        for i in range(nrows):
            if visited[i] == 0:
                self.dfs(i, visited, M)
                count += 1
        return count
    
    def dfs(self, i, visited, M):
        for nei in range(len(M)):
            if M[i][nei] == 1 and visited[nei] == 0:
                visited[nei] = 1
                self.dfs(nei, visited, M)
        
        
M = [[1,1,0],
     [1,1,0],
     [0,0,1]]

print(Solution().findCircleNum(M))