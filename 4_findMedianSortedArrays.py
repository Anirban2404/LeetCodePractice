#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:09:29 2019

@author: anirban-mac
"""

"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n :
            nums1 , nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return 0
        imin = 0
        imax = m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i-1], nums2[j-1])
                    
                if (m + n) % 2 == 1:
                    return maxLeft
                
                if i == m: 
                    minRight = nums2[j]
                elif j == n: 
                    minRight = nums1[i]
                else: 
                    minRight = min(nums1[i], nums2[j])

                return (maxLeft + minRight) / 2.0
        
        
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1,nums2))