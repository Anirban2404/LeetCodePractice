#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:31:25 2019

@author: anirban-mac
"""

"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
            
        print(d1,d2)
        print(sorted(d1.values()), sorted(d2.values()))
        return sorted(d1.values()) == sorted(d2.values())



s = "aba" 
t = "foo"
print(Solution().isIsomorphic(s, t))