#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:40:12 2019

@author: anirban-mac
"""
"""
Given a sorted (in ascending order) integer array nums of n elements 
and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def linearSearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while (start<=end):
            mid = int(start + (end - start)/2)
            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            if nums[mid]>target:
                end = mid - 1
            # Else the element can only be present  
            # in right subarray 
            elif nums[mid]<target:
                start = mid + 1
            else:
                return mid
        return -1
    
    def binarySearch2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearchHelper(nums,0,len(nums)-1,target)
        
    
    def binarySearchHelper (self,nums, start, end, target): 
        # Check base case 
        if start <= end: 
            mid = int(start + (end - start)/2)
            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            if nums[mid] > target: 
                return self.binarySearchHelper(nums, start, mid-1, target) 
            # Else the element can only be present  
            # in right subarray 
            elif nums[mid]<target:
                return self.binarySearchHelper(nums, mid + 1, end, target) 
            else:
                return mid
        return -1
        
    
        
nums = [-1,0,3,5,9,12]
target = 12
#target = 2

print(Solution().linearSearch(nums,target))
print(Solution().binarySearch(nums,target))
print(Solution().binarySearch2(nums,target))