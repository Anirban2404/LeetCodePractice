#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:50:13 2019

@author: anirban-mac
"""
"""
1119. Remove Vowels from a String
Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""

"""
class Solution:
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = ['a','e','i','o','u']
        consonant = 0
        s = list(''.join(S))
        print(s)
        
        for i in range(len(s)):
            if s[i] not in vowels:
                #swap
                if consonant != i:
                    s[consonant], s[i] = s[i], s[consonant] 
                consonant += 1
        return ''.join(s[:consonant]) 
                    
                


S = "leetcodeisacommunityforcoders"
S = ""
print(Solution().removeVowels(S))