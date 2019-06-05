#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:12:59 2019

@author: anirban-mac
"""
"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
       
        max_ending_here = max_so_far = nums[0]
        for x in nums:
            #print(x)
            #print("1:",max_ending_here )
            max_ending_here = max(x, max_ending_here + x)
            #print("1-:",max_ending_here )
            max_so_far = max(max_so_far, max_ending_here)
            #print("2:",max_so_far)
            
        return max_so_far
                
        #return maxsum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
k = 6
print(Solution().maxSubArrayLen(nums,k))
