#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:33:49 2019

@author: anirban-mac
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        if len(s)%2 !=0:
            return False
        stack = []
        brackets = {')':'(', 
                    '}':'{',
                    ']':'['
                   }
        
        for bracket in s:
            print("->", stack)
            if bracket in brackets:
                top = stack.pop() if stack else "#"
                print("Top", top)
                if brackets[bracket] != top:
                    return False
            else:
                stack.append(bracket)
        return not stack

s = "({})({{}})({}[])"     
print(Solution().isValid(s))