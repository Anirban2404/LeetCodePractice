#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:32:23 2019

@author: anirban-mac
"""

"""
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that 
appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is 
also correct.
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant space complexity?
"""

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        res =[]
        print(counter)
        for k, v in counter.items():
            if v == 1:
                res.append(k)
        return res
        
nums =  [1,2,1,3,2,5]
nums = []
print(Solution().singleNumber(nums))