#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:29:25 2019

@author: anirban-mac
"""
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to
 m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        """
        seq1 = 0
        while nums2:
            if seq1 >= m:
                nums1[seq1] = nums2.pop(0)
            elif nums2[0] < nums1[seq1]:
                start = m - 1
                end = seq1 - 1
                for i in range(start, end, -1):
                    nums1[i+1] = nums1[i]
                nums1[seq1] = nums2.pop(0)
                m += 1
            seq1 += 1
        print(nums1)
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
    
nums1 = [1,2,3,8,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1, m, nums2, n))