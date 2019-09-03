#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:32:28 2019

@author: anirban-mac
"""

"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input 
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = {}
        start = 0
        end = 0
        for bracket in s:
            if bracket == "(":
                start += 1
            elif bracket == ")":
                end += 1 if start == 0 else end
                start -= 1 if start > 0 else start
        print(start, end)
        
        def backtrack(s, idx, sc, ec, sr, er, expr):
            if idx == len(s):
                if sr == 0 and er == 0:
                    ans = "".join(expr)
                    output[ans] = 1
            else:
                if (s[idx] == "(" and sr > 0)\
                or (s[idx] == ")" and er > 0):
                    backtrack(s, idx + 1, sc, ec, 
                              sr - (s[idx] == '('),
                              er - (s[idx] == ')'), expr)
                expr.append(s[idx])
                
                
                
        backtrack(s, 0, 0, 0, start, end, [])
        return list(output.keys())
            
            
        
s = "()())()"     
print(Solution().removeInvalidParentheses(s))