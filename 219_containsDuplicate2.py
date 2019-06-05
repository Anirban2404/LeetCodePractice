#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:30:14 2019

@author: anirban-mac
"""

"""
219. Contains Duplicate II
Easy

Given an array of integers and an integer k, find out whether there are two 
distinct indices i and j in the array such that nums[i] = nums[j] and the 
absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ptr1 = 0        

        numarr = {}
        for i,num in enumerate(nums):
            print(i, k + 1) 
            if i > k:
                del numarr[nums[ptr1]]
                ptr1 += 1
            if num in numarr:
                return True
                #print("Found")
            else:
                numarr[num] = i
                

            print(numarr)
        return False

nums = [1,2,3,1,2,3]
k = 20
print(Solution().containsNearbyDuplicate(nums, k))