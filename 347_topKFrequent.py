#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:37:21 2019

@author: anirban-mac
"""

"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count_dict = Counter(nums)
        return heapq.nlargest(k, count_dict.keys(), key = count_dict.get)
        
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))