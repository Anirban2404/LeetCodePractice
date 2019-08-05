#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:26:53 2019

@author: anirban-mac
"""

"""
179. Largest Number
Given a list of non negative integers, arrange them such that they form the 
largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
"""
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        nums = map(str, nums)
        def compareTo(a,b):
            if a+b > b+a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0
        
        nums = sorted(nums, key = cmp_to_key(compareTo), reverse = True)
        res = ''.join(nums)
        res = res.lstrip('0')
        return res if res else "0"
        
nums = [0] 
print(Solution().largestNumber(nums)) #"9534330"