#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:28:01 2019

@author: anirban-mac
"""

"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution 
to such case?
"""
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        dict_s = Counter(s)
        dict_t = Counter(t)
        if dict_s == dict_t:
            print(dict_s,dict_t)
            return True
        return False
        
s = "anagram"
t = "naagram"
print(Solution().isAnagram(s,t))