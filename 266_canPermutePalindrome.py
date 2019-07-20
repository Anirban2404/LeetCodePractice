#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:37:41 2019

@author: anirban-mac
"""

"""
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_s = Counter(s)
        count = 0
        for key, value in dict_s.items():
            count += dict_s.get(key) % 2
            #print(count)
        return count <= 1
    
s = "carerac"
print(Solution().canPermutePalindrome(s))