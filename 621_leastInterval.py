#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:38:35 2019

@author: anirban-mac
"""
"""
Given a char array representing tasks CPU need to do. It contains capital 
letters A to Z where different letters represent different tasks. Tasks could 
be done without original order. Each task could be done in one interval. 
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between 
two same tasks, there must be at least n intervals that CPU are doing different 
tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish 
all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        interval = (longest - 1) * (n + 1)
        for count in counts:
            interval += count == longest and 1 or 0
        return max(len(tasks), interval)
            
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += heap and n or cnt # == if heap then n else cnt
        return ans
        
        """
        
tasks = ["A","A","A","B","B","B"] 
n = 2
print(Solution().leastInterval(tasks,n))