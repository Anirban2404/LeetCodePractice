#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:22:16 2019

@author: anirban-mac
"""

"""
394. Decode String 
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed to 
be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, there won't 
be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = [["", 1]]
        curNum = ""
        for char in s:
            if char.isdigit():
                curNum += char
                print(curNum)
            elif char == '[':
                stack.append(["", int(curNum)])
                curNum = ""
            elif char =="]":
                charEle, numberEle = stack.pop()
                stack[-1][0] += charEle * numberEle
            else:
                stack[-1][0] += char
                print("==>", stack[-1][0])
        
        return stack[0][0]
        
s = "3[a2[bcd]]"
print(Solution().decodeString(s))