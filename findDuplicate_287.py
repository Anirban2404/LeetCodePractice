#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:55:44 2019

@author: anirban-mac
"""

"""
287.Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 
1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated 
more than once.
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict = {}
        for num in nums:
            if num in numdict:
                numdict[num] = numdict[num] + 1
                return (num)
            else:
                numdict[num] = 1
        
        
nums =  [1,3,4,2,2]
print (Solution().findDuplicate(nums))