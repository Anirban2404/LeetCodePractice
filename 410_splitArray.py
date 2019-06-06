#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:15:36 2019

@author: anirban-mac
"""

"""
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you 
can split the array into m non-empty continuous subarrays. Write an algorithm 
to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        print(sum(nums))
        
nums = [7,2,5,10,8]
m = 2
print(Solution().splitArray(nums, m))