#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:28:41 2019

@author: anirban-mac
"""

"""
91. Decode Ways

Share
A message containing letters from A-Z is being encoded to numbers using the 
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of 
ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
#        letterDict = {}
        
        
        if len(s) == 0:
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1 
        
#        for i in range(ord('Z') + 1 - ord('A')):
#            letterDict[i + 1] = chr(i + ord('A'))
        #print(letterDict)
       
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            
            if i != 1 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
                
            print(dp)
        return dp[-1]
                
            

s = "8"
print(Solution().numDecodings(s))