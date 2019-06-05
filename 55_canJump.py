#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:25:27 2019

@author: anirban-mac
"""

"""
55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
#        lastpos = len(nums) - 1
#        for i in range(len(nums) - 1, -1,-1):
#            #print(nums[i])
#            if i + nums[i] >= lastpos:
#                lastpos = i
#        return lastpos == 0
    
    
        maxpos = 0
        for i, n in enumerate(nums):
            if i > maxpos:
                return False
            maxpos = max(maxpos, i+n)
            if maxpos == len(nums) -1:
                return True
            print(i, maxpos)
        return True
        
nums = [1,5,2,1,0,2,0]
print(Solution().canJump(nums))