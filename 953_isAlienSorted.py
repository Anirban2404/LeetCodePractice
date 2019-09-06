#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:08:58 2019

@author: anirban-mac
"""

"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation 
of lowercase letters.

Given a sequence of words written in the alien language, and the order of the 
alphabet, return true if and only if the given words are sorted lexicographicaly 
in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is 
sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], 
hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is 
shorter (in size.) According to lexicographical rules "apple" > "app", because 
'l' > '∅', where '∅' is defined as the blank character which is less than any 
other character (More info).
"""

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_Dict = {}
        i = 1
        for ch in order:
            order_Dict[ch] = i
            i += 1
        #print(order_Dict)
        flag = True
        
        for i in range(len(words) - 1):
            word1 = words[i] 
            word2 = words[i + 1]
            lenw1 = len(word1)
            lenw2 = len(word2)
            
            for j in range(min(lenw1, lenw2)):
                if word1[j] != word2[j]:
                    if order_Dict[word1[j]] > order_Dict[word2[j]]:
                        return False
                    flag = False
                    break

                if flag:
                    if lenw1 > lenw2:
                        return False
        return True
            
        
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))
