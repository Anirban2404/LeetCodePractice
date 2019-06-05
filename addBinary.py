#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:35:42 2019

@author: anirban-mac
"""
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = ""
        carry = 0
        
       
        for i in range(max_len-1, -1, -1):
            res = carry
            res += 1 if a[i] == '1' else 0
            res += 1 if b[i] == '1' else 0
            result = ('1' if res%2 == 1 else '0') + result
            carry = 0 if res < 2 else 1
        
        if carry != 0:
            result = '1' + result
        
        return result.zfill(max_len)
        
            
        
a = "111"
b = "1"
print(Solution().addBinary(a,b))