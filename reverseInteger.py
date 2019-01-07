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
        reversednumber = 0
        number = x
        if (x > 2147483647 or x < -2147483648):
            return 0;
        if x < 0:
            x= -x
        while(x>=1):
            rem = int(x % 10)
            reversednumber = reversednumber*10 + rem
            x = x/10
        #print(reversednumber)
        if (reversednumber > 2147483647 or reversednumber < -2147483648):
            return 0
        if number>=0:
            return reversednumber
        else:
            return -reversednumber

x = 1534236469
print(Solution().reverse(x))