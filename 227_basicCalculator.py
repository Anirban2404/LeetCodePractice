#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:31:44 2019

@author: anirban-mac
"""

"""
227. Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators 
and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
"""
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        stack = []
        num = 0
        sign = "+"
        for i,c in enumerate(s):
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop(-1) * num)
                if sign == "/":
                    tmp = stack.pop(-1)
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else: 
                        stack.append(tmp // num)
                sign = c
                num = 0
        return sum(stack)
        
s = "3+2*2"
print(Solution().calculate(s))