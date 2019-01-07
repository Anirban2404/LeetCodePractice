#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:25:18 2018

@author: anirban-mac
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