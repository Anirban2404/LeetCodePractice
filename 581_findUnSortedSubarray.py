#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:08:56 2019

@author: anirban-mac
"""

"""
581. Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you 
only sort this subarray in ascending order, then the whole array will be sorted 
in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the 
whole array sorted in ascending order.
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        sortedNums = sorted(nums)
#        print(sortedNums)
#        left = 0
#        right = 0
#        for i in range(len(nums)):
#            if nums[i] != sortedNums[i]:
#                left = i
#                break
#            
#        for i in range(len(nums) - 1, -1, -1):
#            if nums[i] != sortedNums[i]:
#                right = i
#                break
#        print(left, right)
#        gap = right - left + 1
#        return gap if gap > 1 else -1
        
                
        minVal = float('inf')
        maxVal = float('-inf')
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                minVal = min(minVal, nums[i])
                maxVal = max(maxVal, nums[i-1])
                
        if minVal == float('inf'):
            return 0
        
        print(minVal, maxVal)
        
        left = 0
        right = len(nums) - 1
        
        while nums[left] <= minVal:
            left += 1
        while nums[right] >= maxVal:
            right -= 1
        print(left,right)
        return right - left + 1
                
nums = [1,5,3,3,2,2,2]
print(Solution().findUnsortedSubarray(nums))