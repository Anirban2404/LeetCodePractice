#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:06:55 2019

@author: anirban-mac
"""
"""
476. Number Complement
Given a positive integer, output its complement number. The complement strategy 
is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), 
and its complement is 0. So you need to output 0.
"""
class Solution:
    def findComplement(self, num):
        complement = 0
        count = 0
        complement_decimal = 0
        
        while num > 1:
            rem = num % 2
            num = num >> 1
      
            rem = 1 if rem == 0 else 0
            
            complement = rem * pow(2, count)
            complement_decimal += complement 
            
            count += 1
        return complement_decimal
    
    
num = 17
print(Solution().findComplement(num))