#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:07:10 2019

@author: anirban-mac
"""

"""
Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which 
gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum_naive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        zeroList = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        numList=(nums[i],nums[j],nums[k])
                        if sorted(numList) not in zeroList:
                            zeroList.append(sorted(numList))
                        
        return(zeroList)
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        target = 6
        for i, num in enumerate(nums[:-2]):
            if i>=1 and num == nums[i-1]:
                continue
            sumdict = {}
           
            complement = target - num
            for j in nums[i+1:]:
                if j not in sumdict:
                    sumdict[complement - j] = j
                else: 
                    res.add((num, complement-j, j))
        print(sumdict)           
        return list(res)
    

    
nums = [-1, 0, 1, 2, -1, 2, 4, 2, 0, 6, 3, 3]
print(Solution().threeSum(nums))