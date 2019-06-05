#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:26:19 2019

@author: anirban-mac
"""

"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of 
strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
       
        lenarr = len(strs)
        if lenarr == 0:
            return ""
        
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

strs = ["flower","flow","flight"]
#strs = ["",""]
print(Solution().longestCommonPrefix(strs))
