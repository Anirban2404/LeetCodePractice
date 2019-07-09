#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:29:30 2019

@author: anirban-mac
"""

"""
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = -1, -1
        shortest = len(words)
        
        if word1 not in words or word2 not in words:
            return -1
        
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            if index1 > -1 and index2 > -1: 
                shortest = min(shortest, abs(index1 - index2))
            #print(shortest, index1, index2)
        return shortest
#
#words = ["a","c","b","a"]
#word1 = "a"
#word2 = "b"
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "practice"
word2 = "coding"
print(Solution().shortestDistance(words, word1, word2))