#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:24:31 2019

@author: anirban-mac
"""

"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume 
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
import re
import math
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.ispalindrome(s, i, i)
            #print(tmp)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.ispalindrome(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
            print(res)
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def ispalindrome(self, s, left, right):
        #print(s, left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left+1:right])
        return s[left+1:right]

s = "babadcbbd"
print(Solution().longestPalindrome(s))