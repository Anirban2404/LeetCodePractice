#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:28:44 2019

@author: anirban-mac
"""

"""
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing 
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
length is 4. 

Input 1:
    A = [1, 2, 1, 5]

Output 1:
    3
    
Explanation 1:
    The sequence : [1, 2, 5]

Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    
Output 2:
    6

Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or 
    [0, 4, 6, 9, 13, 15]
    
Note:

There may be more than one LIS combination, it is only necessary for you to 
return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
import bisect
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) solution
        """
        maxCount = 1
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        
        for i in range(1,len(nums)):
            maxVal = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxVal = max(maxVal, dp[j])
            dp[i] = maxVal + 1
            maxCount = max(maxCount, dp[i])
            print(dp)
        return maxCount
        """
        dp = []
       
        for i in range(len(nums)):
            if len(dp) == 0:
                dp.append(nums[i])
            elif nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                spot = bisect.bisect_left(dp, nums[i], 0, len(dp))
                dp[spot] = nums[i]
            print(dp)
        return len(dp)
                    
        
                
#nums = [1,2,1,5]      
nums = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
#nums = [84,80,27]
#nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))