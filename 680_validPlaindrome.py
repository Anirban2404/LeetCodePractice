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
        start = 0
        end = len(s)
        skip = True
        while start < end:
            if s[start] == s[end - 1]:
                print(s[start], s[end-1])
                start += 1
                end -= 1
            else: 
                if self.isPalindrome(s[start + 1:end]) and skip:
                    return True
                elif self.isPalindrome(s[start:end - 1]) and skip:
                    return True
                else:
                    return False
                skip = False
        return True
        
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        print(s)
        while start < end :
            print(s[start], s[end])
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
        
s = "atbbga"
print(Solution().validPalindrome(s))