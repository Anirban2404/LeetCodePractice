#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:08:36 2019

@author: anirban-mac
"""

"""
33_Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    
    def find_pivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            pivot = (start + end) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[end]:
                    end = pivot 
                else:
                    start = pivot + 1
        return 0   
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        pivot = self.find_pivot(nums)
        print("Pivot:", pivot)
        print(nums[pivot], target)
        if nums[pivot] == target:
            return pivot
        if pivot == 0:
            index = self.searchHelper(nums,target)
            if index == -1:
                return -1
            else:
                return index 
        elif nums[0] > target:
            print("Second")
            index = self.searchHelper(nums[pivot:],target)
            if index == -1:
                return -1
            else:
                return index + pivot
        else:
            print("First")
            index = self.searchHelper(nums[:pivot],target)
            if index == -1:
                return -1
            else:
                return index 
      
        
    def searchHelper(self, nums, target):
        start = 0
        end = len(nums) - 1
        print(nums)
        
        while start <= end:
            mid = (start + end)//2
            #print (start, end, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
nums = [8,9,2,3,4]
target = 2
print(Solution().search(nums, target))
#print(Solution().find_pivot(nums))