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
       
        if len(s)%2!=0:
            return False
        
        else:
            stack = []
            brackets = {")":"(",
                        "}":"{",
                        "]":"[",
                        }
            for char in s:
                if char in brackets and len(stack)>0:
                    #print (char, brackets[char])
                    if brackets[char] == stack[-1]:
                        #print (char, brackets[char])
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
                  
        if len(stack)==0:
            return True
        else:
            return False

s = "){"     
print(Solution().isValid(s))