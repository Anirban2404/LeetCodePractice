#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:39:05 2019

@author: anirban-mac
"""
"""
868. Binary Gap
Given a positive integer N, find and return the longest distance between two 
consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive p
airs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
"""
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        last = None
        count = 0
        for i in range(32) :
            #print(i, N>>i, bin(N>>i).replace("0b",''), N>>i & 1)
            if (N>>i) & 1:
                if last is not None:
                    count = max(count, i - last)
                last = i
        return count
                
        

N = 1041
print(Solution().binaryGap(N))