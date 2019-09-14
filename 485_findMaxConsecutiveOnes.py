#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:29:24 2019

@author: anirban-mac
"""
"""
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0
        return maxCount
    
    
nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))

