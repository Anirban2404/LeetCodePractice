#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:07:02 2019

@author: anirban-mac
"""
"""
Problem 344
Write a function that reverses a string. The input string is given as an array
 of characters char[].

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



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
        i, j  = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)
        
        """
        def reverseString(self, s):
            l = len(s)
            if l < 2:
                return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
        """

#s = ["A man, a plan, a canal: Panama"]
s = ["h","e","l","l","o"]
print(Solution().reverseString(s))