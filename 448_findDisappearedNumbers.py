#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:15:27 2019

@author: anirban-mac
"""

"""
448. Find All Numbers Disappeared in an Array


Share
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the 
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
#from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        counter = Counter(nums)
        res = []
        for i in range(1, len(nums) + 1):
            print(i)
            if i not in counter:
                res.append(i)
        return res
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i in range (len(nums)) if nums[i] > 0]

nums = [4,3,2,7,8,2,3,1]

print(Solution().findDisappearedNumbers(nums))