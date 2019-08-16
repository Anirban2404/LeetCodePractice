#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:38:33 2019

@author: anirban-mac
"""

"""
Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
class Solution:
    def jump(self, nums):
        length = len(nums) - 1
        jumps = 0
        maxPos = 0
        nextmaxPos = 0
        
        if length == 0:
            return 0
        
        for i, num in enumerate(nums):
            if maxPos >= length:
                break
            if maxPos < i:
                maxPos =  nextmaxPos
                jumps += 1
                if maxPos < i:
                    return -1
            nextmaxPos = max(nextmaxPos, i + num)
            
        return jumps
    
nums = [2,1,11,1,4,0,0,0,0,0,4,1,0]
print(Solution().jump(nums))