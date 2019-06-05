#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:25:44 2019

@author: anirban-mac
"""

"""
Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCountOnes = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            if maxCountOnes < count:
                maxCountOnes = count
        return maxCountOnes
                
        
nums = [1,1,0,1,2,1,1]
print(Solution().findMaxConsecutiveOnes(nums))