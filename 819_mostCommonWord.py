#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:16:41 2019

@author: anirban-mac
"""

"""
819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word 
that is not in the list of banned words.  It is guaranteed there is at least 
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of 
punctuation.  Words in the paragraph are not case sensitive.  The answer is in 
lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent 
non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""
from functools import reduce
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        repls = {'!':' ',
         ',':' ', 
         '?':' ', 
         '\'':' ',
         ';':' ',
         '.':' '
         }
        paragraph = reduce(lambda a, kv: a.replace(*kv), repls.items(), \
                           paragraph.lower())
        para_dict = Counter(paragraph.split(' '))
        for key, value in sorted(para_dict.items(), key = lambda x: x[1], \
                                 reverse = True):
            print(key,value)
            if key not in banned and key != '':
                return key
        return ""
        
        
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))