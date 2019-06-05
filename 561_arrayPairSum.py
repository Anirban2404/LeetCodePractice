#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:14:15 2019

@author: anirban-mac
"""

"""
561.Array Partition I

Given an array of 2n integers, your task is to group these integers into n 
pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of 
min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        nums = sorted(nums)
        sum = 0
        for i in range(0,len(nums),2):
            sum = sum + nums[i]
        return sum
        
nums = [7,3,1,0,0,6]
nums = [1, 2, 5, 6, 7, 9]
nums = [1,2]
print(Solution().arrayPairSum(nums))