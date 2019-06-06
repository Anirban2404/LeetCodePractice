#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:41:52 2019

@author: anirban-mac
"""

"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        localmin = localmax = maxproduct = nums[0]
        for x in nums[1:]:
            if x < 0:
                localmin, localmax = localmax, localmin
            localmax = max(x, localmax * x)
            localmin = min(x, localmin * x)
            maxproduct = max(maxproduct, localmax)
            print(localmax, localmin, maxproduct)
        return maxproduct

nums = [2,3,-2,-6]
print(Solution().maxProduct(nums))