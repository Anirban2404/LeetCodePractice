#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:25:18 2018

@author: anirban-mac
"""

"""
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (target == nums[i] + nums[j] and i!=j):
                    print(i,j)
                    return(i,j)
                    
    def twoSumHash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumdict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            print(sumdict)
            print(complement,sumdict.keys())
            if num in sumdict:
                return (sumdict[num], i)
#            sumdict[complement] = i
            sumdict[complement] = i
        return (-1, -1)
        
            
nums = [3,2,4,4,5]
target = 9
print(Solution().twoSum(nums,target))
print(Solution().twoSumHash(nums,target))