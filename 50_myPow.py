#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:14:38 2019

@author: anirban-mac
"""
"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n & 1 == 1: #n%2 == 1
                res *= x
            x *= x
            n >>= 1 #n = n/2
        return res
x = 2.0
n = 4
print(Solution().myPow(x,n))