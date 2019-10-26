#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:24:43 2019

@author: anirban-mac
"""
"""
323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge 
is a pair of nodes), write a function to find the number of connected components 
in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges 
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together 
in edges.
"""
from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for edge in edges:
            src, dst = edge
            graph[src].append(dst)
            graph[dst].append(src)
        
        #print(graph)
        visited = {}
        
        def dfs(node):
            if node in visited:
                return 
            
            if node in graph:
                visited[node] = 1
                for neighbor in graph[node]:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        #print(visited, count)
        return count
        
n = 4 
edges = [[2,3],[1,2],[1,3]]
print(Solution().countComponents(n, edges))
