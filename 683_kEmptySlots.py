#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:55:46 2019

@author: anirban-mac
"""
"""
683. K Empty Slots

There is a garden with N slots. In each slot, there is a flower. The N flowers 
will bloom one by one in N days. In each day, there will be exactly one flower 
blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array 
represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i 
will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two 
flowers in the status of blooming, and also the number of flowers between them 
is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become 
blooming.

Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1

Note:
The given array will be in the range [1, 20000].
"""

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
   
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
        print (days)   
        ans = 0
        left, right = 0, k + 1
        #while right < len(days):
            #for i in range(left + 1, right):
                
        
flowers = [2, 3, 4, 5, 10, 6, 7, 1, 8, 9]
k = 4
print(Solution().kEmptySlots(flowers, k))