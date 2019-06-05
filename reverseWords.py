#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:03:35 2019

@author: anirban-mac
"""

"""
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        reversedWords = ""
        words = s.strip().split(" ")
        reversedWordList = []
    
        for i in range(len(words)-1, -1, -1):
            if len(words[i].strip()) != 0:
                reversedWordList.append(words[i].strip())
        print(reversedWordList)
        reversedWords = ' '.join(reversedWordList)
        return reversedWords.strip()
            
s = "   a     b "
print(Solution().reverseWords(s))

