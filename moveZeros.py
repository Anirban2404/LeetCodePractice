#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:12:59 2019

@author: anirban-mac
"""
"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution:
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       
        
        nonzeroIndex = 0

        for i in range(len(nums)):
            print(i)
            if (nums[i]!=0):
                print("nonzeroIndex", nonzeroIndex)
                if nonzeroIndex!=i : #swap
                    nums[nonzeroIndex] = nums[i]
                    nums[i] = 0
                nonzeroIndex += 1
        print(nums)
        
        
            
nums = [0,1,0,3,12]

print(Solution().moveZeroes(nums))
