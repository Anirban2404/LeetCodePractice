#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:50:48 2019

@author: anirban-mac
"""

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a 
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only 
the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
  
        small = 1
        big = x//2 + 1
        while small <= big:
            mid = (small + big)//2
            print(small, big)
            if x / (mid * mid) == 1:
                return mid
            elif x > (mid * mid):
                small = mid + 1
            else:
                 big = mid - 1
        return (big + small) // 2
    
        """
        for i in range(x):
            result = i * i
            if result > x:
                return i - 1
        """
        
        
        
x = 82
print(Solution().mySqrt(x))