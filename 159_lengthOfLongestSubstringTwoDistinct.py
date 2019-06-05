#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:08:33 2019

@author: anirban-mac
"""

"""

159 . Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at 
most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if n < 3:
            return n
        
        basket = collections.Counter()
        maxLen = 2
        maxval = local = 0
        for i, alph in enumerate(s):
            basket[alph] += 1
            while len(basket)>=maxLen+1:
                basket[s[local]] -= 1
                if basket[s[local]] == 0:
                    del basket[s[local]]
                local += 1
            maxval = max(maxval, i - local + 1)
        return maxval
            

s = "eceba"
print(Solution().lengthOfLongestSubstringTwoDistinct(s))