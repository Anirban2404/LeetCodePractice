#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:32:22 2019

@author: anirban-mac
"""
"""
451. Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from collections import Counter
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
#        sortedList = sorted(sorted(s), key = Counter(s).get, reverse = True)
#        return ''.join(sortedList)
        #s = sorted(s)
        counter = Counter(s)
        res = ""
        sortedCounter=counter.most_common()
        #print(counter,sortedCounter)
        
        for letter,freq in sortedCounter:
            res += letter * freq
        return res
        
s = "cccaaa"
print(Solution().frequencySort(s))