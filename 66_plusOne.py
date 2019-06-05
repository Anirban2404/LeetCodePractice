#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:01:58 2019

@author: anirban-mac
"""
"""
Given a non-empty array of digits representing a non-negative integer, plus 
one to the integer.

The digits are stored such that the most significant digit is at the head of 
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 
0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lenDigits = len(digits)
        for i in range(lenDigits - 1, -1, -1):
            # add 1 
            digits[i] +=1
            if digits[i] < 10:
                return digits
            else:
                digits [i] = 0
                
        # if 0th digit is 9
        if digits[i] == 0:
            digits.insert(0,1)
            return digits
                
        
        
digits = [1, 9, 9, 9]
print(Solution().plusOne(digits))