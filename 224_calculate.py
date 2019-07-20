#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:44:50 2019

@author: anirban-mac
"""
"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + 
or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
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
        n = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                num = 10 ** n * (ord(s[i]) - ord('0')) + num
                n += 1
                
            elif not s[i].isspace():
                if n :
                    stack.append(num)
                    print(stack)
                    n = 0
                    num = 0
                if s[i] == "(":
                    res = self.evaluate(stack)
                    stack.pop()
                    stack.append(res)
                    print(stack)
                else:
                    stack.append(s[i])
        if n:
            stack.append(num)
        return self.evaluate(stack)
    
    def evaluate(self, stack):
        res = stack.pop() if stack else 0
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res
                
        
                
s = "14-(5 - 12 - 1)"
print(Solution().calculate(s))