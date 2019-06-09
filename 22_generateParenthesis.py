#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 22:07:02 2019

@author: anirban-mac
"""
"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                res.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')' , left, right + 1)
        backtrack('', 0 , 0)
        return res

n = 3
print(Solution().generateParenthesis(n))