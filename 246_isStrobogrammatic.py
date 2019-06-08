#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:22:50 2019

@author: anirban-mac
"""

"""
246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is 
represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'1':'1', 
               '0':'0', 
               '6':'9', 
               '8':'8',
               '9':'6'}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in dic or dic[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
        
    
n = "67"
print(Solution().isStrobogrammatic(n))