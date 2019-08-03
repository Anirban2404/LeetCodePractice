#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:53:20 2019

@author: anirban-mac
"""

"""
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number 
of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""

from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        count = 0
        for i in range(len(nums)):
            summ = nums[i]
            if nums[i] == k:
                count += 1
            for j in range(i + 1, len(nums)):
                summ = summ + nums[j]
                print(summ)
                if (summ == k):
                    count += 1
        return count
        """
        cumSum = 0
        sumDict = defaultdict(int)
        sumDict[0] = 1
        count = 0
        for num in nums:
            cumSum += num
            diff = cumSum - k
            if diff in sumDict:
                count += sumDict[diff]
            sumDict[cumSum] += 1
        return count
        
        
nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
print(Solution().subarraySum(nums, k))
