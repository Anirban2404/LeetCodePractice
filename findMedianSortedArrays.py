#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:26:25 2019

@author: anirban-mac
"""

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        avgnums1 = 0
        avgnums2 = 0
        count1 = 1
        count2 = 1
        
 
        
        avgnums1 = sum(nums1)/count1
        avgnums2 = sum(nums2)/count2
        
        
        median = (avgnums1 + avgnums2)/2
        return median
    
nums1 = []
nums2 = [1]
 
print(Solution().findMedianSortedArrays(nums1,nums2))