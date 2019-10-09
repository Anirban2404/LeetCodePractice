#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:59:34 2019

@author: anirban-mac
"""

"""
72. Edit Distance
Given two words word1 and word2, find the minimum number of operations required 
to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
#from collections import defaultdict
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)
        if m == 0: 
            return n 
   
        if n == 0: 
            return m 
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        print(dp)
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]
#            
#        def helper(str1, str2) :
#            m = len(str1)
#            n = len(str2)
#            if m == 0: 
#                return n 
#   
#            if n == 0: 
#                return m 
#            
#            #print(str1, str2)
#            if str1[m-1] == str2[n-1]: 
#                return helper(str1[:m-1], str2[:n-1]) 
#            
#            return 1 + min(helper(str1[:m], str2[:n-1]),    # Insert 
#                   helper(str1[:m-1], str2[:n]),    # Remove 
#                   helper(str1[:m-1], str2[:n-1])    # Replace 
#                   ) 
#            
#        
#        return helper(word1, word2) 
        

        
        
word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))