#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:12:40 2019

@author: anirban-mac
"""

"""
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the 
order among letters are unknown to you. You receive a list of non-empty words 
from the dictionary, where words are sorted lexicographically by the rules of
this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
"""

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        alienDict = []
        alienCharOrder = []
        alienChars = set(''.join(words))
    
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            lenw1 = len(word1)
            lenw2 = len(word2)
            
            for j in range(min(lenw1, lenw2)):
                if word1[j] != word2[j]:
                    alienDict.append(word1[j] + word2[j])
                    break
                
        while alienDict:
            free = alienChars - {pair[1] for pair in alienDict}
            #print(free, "||", alienDict)
            if not free:
                print("Hi")
                return ''
            
            alienCharOrder += list(free)
            alienDict = [pair for pair in alienDict if free.isdisjoint(pair)]
            #alienDict = filter(free.isdisjoint, alienDict)
            alienChars -= free
            #print(alienCharOrder)
            
        print(list(alienCharOrder))
        return ''.join(alienCharOrder + list(alienChars))
            
           
words = ["wrt","wrf","er","ett","rftt"]
#words = ["a","b", "a"]
print(Solution().alienOrder(words))