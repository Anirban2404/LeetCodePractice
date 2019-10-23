#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:40:38 2019

@author: anirban-mac
"""

"""
310. Minimum Height Trees
For an undirected graph with tree characteristics, we can choose any node as the 
root. The result graph is then a rooted tree. Among all possible rooted trees, 
those with minimum height are called minimum height trees (MHTs). Given such a 
graph, write a function to find all the MHTs and return a list of their root 
labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given 
the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges 
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together 
in edges.
Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
"""
from collections import defaultdict , Counter, deque

class Solution:    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        degree = Counter()
        q = deque()
        
        if len(edges) == 0:
            return [0]
        
        for edge in edges:
            parent, child = edge
            graph[parent].append(child)
            graph[child].append(parent)
            degree[parent] += 1      
            degree[child] += 1      
        
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
#        print(degree)
#        print(q)
        while n > 2:
            for i in range(len(q)):
                leaf = q.popleft()
                n -= 1
                
                for j in graph[leaf]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        q.append(j)
        res = []
        while len(q) > 0: 
            res.append(q.popleft()) 
  
        return res
                
            
        
n = 6
edges = [[1, 0], [1, 2], [1, 3]]
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(Solution().findMinHeightTrees(n, edges))