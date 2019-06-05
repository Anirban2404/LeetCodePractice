#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:15:48 2019

@author: anirban-mac
"""
"""
724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index 
of this array.

We define the pivot index as the index where the sum of the numbers to the left 
of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot 
indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum 
of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tot = sum(nums)
        leftsum = 0
        #print(tot)
        for i in range(len(nums)):
            #print(nums[:i])
            #print(nums[i])
            
            #print(leftsum, (tot - leftsum - nums[i]))
            if leftsum == (tot - leftsum - nums[i]):
                return i
            leftsum += nums[i]
        return -1


        
nums = [-5,-8,0,8,5,3,-3,0]
print(Solution().pivotIndex(nums))