#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:44:53 2019

@author: anirban-mac
"""

"""
220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i 
and j in the array such that the absolute difference between nums[i] and nums[j] 
is at most t and the absolute difference between i and j is at most k.

This problem requires us to find ii and jj such that the following conditions 
are satisfied:
1. |i - j| <= k
2. | nums[i] - nums[j] | <= t 
 
Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        cache = {}
        for i in range(len(nums)):
            if i-k > 0:
                bucket_id_to_delete = nums[i-k-1]//(t+1)
                del cache[bucket_id_to_delete]
            bucket_id = nums[i]//(t+1)
            print(bucket_id)
            condition1 = (bucket_id in cache)
            condition2 = ((bucket_id-1 in cache and abs(cache[bucket_id-1]-nums[i])<= t))
            condition3 = ((bucket_id+1 in cache and abs(cache[bucket_id+1]-nums[i])<= t))
            if condition1 or condition2 or condition3:
                return True
            cache[bucket_id] = nums[i]
            print(cache)
        return False
    
nums = [2,7,4,6,1,8,9]
k = 3
t = 1
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))