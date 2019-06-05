#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:32:05 2019

@author: anirban-mac
"""

"""
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not 
be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitwords = s.split(" ")
        reverseSen = []
        for word in splitwords:
            reverseSen.append(self.reverse(word))
        reverseSen = ' '.join(reverseSen)
        return reverseSen
    
    def reverse(self, word):
        chars = list(word)
        start = 0
        end = len(word) - 1
        while (start < end):
            chars[start],chars[end] = chars[end],chars[start]
            start += 1
            end -= 1
        return ''.join(chars)
        
    
s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))