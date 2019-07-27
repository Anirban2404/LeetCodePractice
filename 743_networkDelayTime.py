#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:59:28 2019

@author: anirban-mac
"""
"""
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), 
where u is the source node, v is the target node, and w is the time it takes 
for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes 
to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""

from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, N + 1)}
        print(dist)
        seen = [False] * (N + 1)
        dist[K] = 0
        
        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            
            if cand_node < 0:
                break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
                
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))