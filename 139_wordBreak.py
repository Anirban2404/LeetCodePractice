#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:46:58 2019

@author: anirban-mac
"""
"""
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of 
non-empty words, determine if s can be segmented into a space-separated sequence 
of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen 
apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
            print(dp)
        return dp[-1]
        
s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))