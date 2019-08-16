#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:57:29 2019

@author: anirban-mac
"""
"""
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains 
the permutation of s1. In other words, one of the first string's permutations 
is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Counter = defaultdict(int)
        s2Counter = defaultdict(int)
        if len(s1) > len(s2):
            return
        
        for i in s1:
           s1Counter[i] += 1
           
        for i in s2[:len(s1)]:
            s2Counter[i] += 1
        
        lptr = 0
        rptr = len(s1)
    
        while rptr < len(s2):
            if s1Counter == s2Counter:
                return True
            s2Counter[s2[lptr]] -= 1
            if s2Counter[s2[lptr]] < 1:
                del s2Counter[s2[lptr]]
            s2Counter[s2[rptr]] += 1
            lptr += 1
            rptr += 1
        
        return s1Counter == s2Counter
            
         
        
            
s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1,s2))