#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:55:48 2019

@author: anirban-mac
"""

"""
Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant extra space complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumRange = len(nums)*(len(nums)+1)//2
        missingNum = sumRange - sum(nums)
        return missingNum
        
        
nums = [9,6,4,2,3,5,7,0,1]

print(Solution().missingNumber(nums))