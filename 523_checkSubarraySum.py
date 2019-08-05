#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:16:03 2019

@author: anirban-mac
"""

"""
523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function 
to check if the array has a continuous subarray of size at least 2 that sums up 
to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and 
sums up to 42.
"""
from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        cumSum = 0
        sumDict = defaultdict(int)
        sumDict[0] = -1

        for i, num in enumerate(nums):
            cumSum += num
            print(cumSum)
            if k != 0:
                cumSum = cumSum % k
            print(cumSum)
            if cumSum not in sumDict:
                sumDict[cumSum] = i
            else:
                if i - sumDict[cumSum] >= 2:
                    return True
        return False
    
nums = [23, 2, 4, 6, 4, 7]  
k = -6
print(Solution().checkSubarraySum(nums, k))