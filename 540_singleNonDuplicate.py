#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:49:45 2019

@author: anirban-mac
"""

"""
540. Single Element in a Sorted Array
Given a sorted array consisting of only integers where every element appears 
twice except for one element which appears once. Find this single element 
that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

"""

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        numdict = {}
        for num in nums:
            if num in numdict:
                numdict[num] = numdict[num] + 1
            else:
                numdict[num] = 1
        #print(numdict)
        for key, value in numdict.items():
            if value == 1:
                return key
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if mid%2 ==0:
                mid +=1
            if nums[mid] == nums[mid - 1]:
                low = mid + 1   
            else:
                high = mid - 1   
        return nums[low]
            
        
        
nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))

