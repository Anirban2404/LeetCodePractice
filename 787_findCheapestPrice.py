#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:20:09 2019

@author: anirban-mac
"""
"""
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and 
arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the 
destination dst, your task is to find the cheapest price from src to dst with 
up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as 
marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as 
marked blue in the picture.
"""
from collections import defaultdict
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(dict)
        for u,v,w in flights:
            graph[u][v] = w
        print(graph)
        
        optimal = {}
        heap = [(0, 0, src)]
        while heap:
            #print(optimal)
            cost, k, cur_node = heapq.heappop(heap)
            #print(optimal.get((k, cur_node), float('inf')))
            if k > K + 1 or cost > optimal.get((k, cur_node), float('inf')):
                continue
                
            if cur_node == dst:
                return cost
            
            for neighbor, wt in graph[cur_node].items():
                newCost = cost + wt
                if newCost < optimal.get((k+1, neighbor), float('inf')):
                    heapq.heappush(heap, (newCost, k+1, neighbor))
                    optimal[k+1, neighbor] = newCost
                print(optimal)
        return -1
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0 
dst = 2
k = 0
print(Solution().findCheapestPrice(n, edges, src, dst, k))