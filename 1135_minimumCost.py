#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:40:04 2019

@author: anirban-mac
"""
"""
1135. Connecting Cities With Minimum Cost
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] 
represents the cost to connect city1 and city2 together.  (A connection is 
bidirectional: connecting city1 and city2 is the same as connecting city2 
and city1.)

Return the minimum cost so that for every pair of cities, there exists a path 
of connections (possibly of length 1) that connects those two cities together. 
The cost is the sum of the connection costs used. If the task is impossible, 
return -1.

 

Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.

"""
# Finding Minimum spanning Tree 

from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, N, connections):
        graph = defaultdict(list)
        start = connections[0][0]
        for src, dst, wt in connections:
            graph[src].append((dst, wt))
            graph[dst].append((src, wt))
         
        print(graph)
        dist = {}
        heap = [(0, start)]
        while heap:
            ddist, node = heapq.heappop(heap)
            print(ddist, node)
            if node in dist:
                continue
            dist[node] = ddist
            for neighbor, d in graph[node]:
                if neighbor not in dist:
                    heapq.heappush (heap, (d, neighbor))
        print(dist)
        return sum(dist.values()) if len(dist) == N else -1
        
N = 3
connections = [[1,2,5],[1,3,6],[2,3,1]]
print(Solution().minimumCost(N, connections))