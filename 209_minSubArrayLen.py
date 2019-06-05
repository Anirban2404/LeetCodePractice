#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:32:27 2019

@author: anirban-mac
"""
"""
209. Minimum Size Subarray Sum
 
Given an array of n positive integers and a positive integer s, find the 
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't 
one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem 
constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of 
which the time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) + 1
        summ = 0

        for i in range(len(nums)):
            summ = summ + nums[i]
            while summ >= s:
                end = min(end, i + 1 - start)
                #print (end)
                # Subtract nums[start] from sum and increment start
                summ = summ - nums[start]
                start += 1
        
        return end if end != len(nums) + 1 else 0
    
s = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(s, nums))