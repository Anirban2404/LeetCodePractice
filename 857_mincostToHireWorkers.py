#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:48:59 2019

@author: anirban-mac
"""

"""
857. Minimum Cost to Hire K Workers
There are N workers.  The i-th worker has a quality[i] and a minimum wage 
expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group 
of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality 
compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage 
expectation.
Return the least amount of money needed to form a paid group satisfying the 
above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers 
seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""
import heapq
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        print(workers)
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            print(r,q)
            heapq.heappush(heap, -q)
            qsum += q
            print("sum-->", qsum)
            if len(heap) > K: 
                top = heapq.heappop(heap)
                print("-->", top)
                qsum += top
                print("::>", float(qsum))
            if len(heap) == K: 
                res = min(res, qsum * r)
            print(";;-->",res)
        return res
        
       
quality = [10,20,5]
wage = [70,50,30]
K = 2
        
print(Solution().mincostToHireWorkers(quality, wage, K))