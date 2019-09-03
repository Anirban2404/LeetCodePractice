#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:15:35 2019

@author: anirban-mac
"""
"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge
whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of 
the string is 50000.
"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
s = "abca"
print(Solution().validPalindrome(s))