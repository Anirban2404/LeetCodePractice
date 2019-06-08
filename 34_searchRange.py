#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:47:50 2019

@author: anirban-mac
"""

"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting 
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.binarySearch(nums, target, True)
        if idx == len(nums) or nums[idx] != target:
            return [-1, -1]
        return [idx, self.binarySearch(nums, target, False) - 1]
        
    def binarySearch(self, nums, target, flag):
        left = 0
        right = len(nums) 
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (flag and target == nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left

            
        
        
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))