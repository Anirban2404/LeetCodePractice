#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:55:17 2019

@author: anirban-mac
"""

"""
532. K-diff Pairs in an Array
Given an array of integers and an integer k, you need to find the number of 
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer 
pair (i, j), where i and j are both numbers in the array and their absolute 
difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of 
unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) 
and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

"""

import collections
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        counter = collections.Counter(nums)
        #print(counter)
        for i in counter:
            if (k > 0 and i + k in counter) \
            or (k == 0 and counter[i] > 1):
                count += 1
        return count
    
#Run tests
nums = [0,0,1,0,0]
k = 1
print(Solution().findPairs(nums, k))