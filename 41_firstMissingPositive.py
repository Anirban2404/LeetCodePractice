#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:33:45 2019

@author: anirban-mac
"""

"""
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
#from collections import Counter
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        if len(nums) == 0:
#            return 1
#        counter = Counter(nums)
#        
#        for i in range(1, len(nums) + 2):
#            if i not in counter:
#                return i
#        return 1
        nums.append(0)
        
        n = len(nums)
        print(n)
        #delete those useless elements
        for i in range(len(nums)): 
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        print(nums)      
        
        #use the index as the hash to record the frequency of each number
        for i in range(len(nums)): 
            nums[nums[i] % n] += n
            print(nums)
        
        for i in range(1,len(nums)):
            if nums[i]//n == 0:
                return i
        
        return n
        
nums = [2,2]
print(Solution().firstMissingPositive(nums))