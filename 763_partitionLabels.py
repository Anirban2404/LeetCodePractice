#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:49:04 2019

@author: anirban-mac
"""

"""
763. Partition Labels
A string S of lowercase letters is given. We want to partition this string into 
as many parts as possible so that each letter appears in at most one part, and 
return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits 
S into less parts.
"""
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}
        for i,char in enumerate(S):
            last[char] = i
        print(last)
        ans = []
        # last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        for i, char in enumerate(S):
            print(j)
            j = max(j, last[char])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
    
S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))