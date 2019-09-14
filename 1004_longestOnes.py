#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:10:35 2019

@author: anirban-mac
"""

"""
1004. Max Consecutive Ones III
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
"""

class Solution:
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, j = 0, 0
        maxl, maxr = 0, 0
        while j < len(A):
            if A[j] == 0:
                K -= 1
                while i <= j and K < 0:
                    K += 1 if A[i] == 0 else 0
                    i += 1
            j += 1
            if j - i > maxr - maxl:
                maxl, maxr = i, j
        return maxr - maxl 
            
            
A = [0,1,0,1,0,1]
K = 2
print(Solution().longestOnes(A, K))