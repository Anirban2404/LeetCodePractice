#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:43:52 2019

@author: anirban-mac
"""
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversedInteger = 0
        number = x
        if (x > 2147483647 or x < -2147483648):
            return 0
        if x < 0:
            x = -x
        while x >= 1:
            reversedInteger = reversedInteger * 10 + x % 10
            x = x // 10
        if (reversedInteger > 2147483647 or reversedInteger < -2147483648):
            return 0
        if number >= 0:
            return reversedInteger
        else:
            return -reversedInteger
            

x = 14236469
print(Solution().reverse(x))