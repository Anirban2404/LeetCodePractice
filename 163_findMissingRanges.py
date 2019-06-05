#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:37:15 2019

@author: anirban-mac
"""

"""
Missing Ranges

Given a sorted integer array nums, where the range of elements are in the 
inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        diff = 0
        ranges = []
        if len(nums) < 1:
            if upper == lower:
                return str(lower)
            outstr = str(lower) + "->" + str(upper)
            ranges.append(outstr)
            return ranges
        
        if nums[0] != lower:
            if nums[0] - lower < 2:
                ranges.append(str(nums[0] - 1))
            else:
                outstr = str(lower) + "->" + str(nums[0] - 1)
                ranges.append(outstr)
                
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 0 or diff == 1:
                continue
            if diff <= 2:
                ranges.append(str(nums[i] - 1))
            else:
                outstr = str(nums[i-1] + 1) + "->" + str(nums[i] - 1)
                ranges.append(outstr)
                
        if nums[len(nums)-1] != upper:
            if upper - nums[len(nums)-1] == 1:
                ranges.append(str(upper))
            else:
                outstr = str(nums[len(nums)-1] + 1) + "->" + str(upper)
                ranges.append(outstr)

        return ranges
            
            
            
nums = [1,1,1,1]
lower = 0
upper = 3
print(Solution().findMissingRanges(nums, lower, upper))