#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:11:12 2019

@author: anirban-mac
"""

"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating 
characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence 
             and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
class Solution:
    # Sliding Window
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        newalphabets = []
        maxcount = 0
        
        for i in s:

            if i not in newalphabets:
                newalphabets.append(i)
                
            else:
                newalphabets = newalphabets[newalphabets.index(i)+1:]
                newalphabets.append(i)
            #print(newalphabets, "-->", len(newalphabets))
            if maxcount < len(newalphabets):
                maxcount = len(newalphabets)
                
        return (maxcount)
    
    # Sliding Window Hashmap
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        newalphabets = {}
        maxcount = 0
        ans = 0
        for i,alph in enumerate(s):
            if alph in newalphabets:
                maxcount =  max(maxcount, newalphabets.get(alph))
                print("::",newalphabets.get(alph))
                print(maxcount, i)
                print(newalphabets)
            ans = max(ans, i - maxcount + 1)
            newalphabets[alph] = i + 1
             
#            print(newalphabets, "-->",i,maxcount  ,ans)
        return (ans)
        
s = "abbbba"
#print(Solution().lengthOfLongestSubstring(s))
print(Solution().lengthOfLongestSubstring2(s))
