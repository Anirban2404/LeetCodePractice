#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:35:06 2019
Problem 186. Reverse Words in a String II
@author: anirban-mac
"""

"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?

"""

class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        
        rcounter = 0
        lcounter = len(str) - 1
       
        self.reverseString(str, rcounter, lcounter)
       
        # 2, reverse each word
        for i in range(len(str)):
            if str[i] == " ":
                self.reverseString(str, rcounter, i - 1)
                rcounter = i + 1
            elif i == len(str) - 1:
                self.reverseString(str, rcounter, i)
  
        print (str)
        
    def reverseString(self, s, rcounter, lcounter):
        """
        :type s: str
        :rtype: str
        """
        
        while rcounter < lcounter:
            s[rcounter], s[lcounter] = s[lcounter], s[rcounter]
            rcounter += 1
            lcounter -= 1
            
str = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(Solution().reverseWords(str))