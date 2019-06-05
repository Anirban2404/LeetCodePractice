#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:54:13 2019

@author: anirban-mac
"""
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
import time
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numarr = {}
        i = 0
        for num in nums:
            if num not in numarr:
#                numarr.append(num)
                numarr[num] = i
                i = i + 1
            else:
                return True
        print(numarr)
        return False

nums = [1,2,2,3,4]
start = time.time()
print(Solution().containsDuplicate(nums))
end = time.time()
print(end-start)