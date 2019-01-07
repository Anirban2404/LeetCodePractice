#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:07:02 2019

@author: anirban-mac
"""
"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverseString = []
        origString = list(s)
        for i in range(len(origString)-1,-1,-1):
           reverseString.append(origString[i]) 
        #print(reverseString)
        reverseString = ''.join(reverseString)
        return(reverseString)

s = "A man, a plan, a canal: Panama"
print(Solution().reverseString(s))