#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:03:54 2019

@author: anirban-mac
"""

"""
47. Permutations II
Given a collection of numbers that might contain duplicates, return all 
possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from collections import defaultdict

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(first):
            if first == n:
                if tuple(nums) not in seen:
                    output.append(nums[:])
                    seen[tuple(nums[:])] = 1
                
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        seen = defaultdict(list)
        output = []
        backtrack(0)
        return output

nums = [1, 1, 2]
print(Solution().permuteUnique(nums))