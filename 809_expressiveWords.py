#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:55:10 2019

@author: anirban-mac
"""

"""
809. Expressive Words
Sometimes people repeat letters to represent extra feeling, such as 
"hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", 
we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal 
to S by any number of applications of the following extension operation: choose 
a group consisting of characters c, and add some number of characters c to the 
group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" 
to get "hellooo", but we cannot get "helloo" since the group "oo" has size less 
than 3.  Also, we could do another extension like "ll" -> "lllll" to get
"helllllooo".  If S = "helllllooo", then the query word "hello" would be 
stretchy because of these two extension operations: 
query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 
or more.
"""
class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return sum(self.check(S, W) for W in words)

    def check(self, S, W):
        i, j, n, m = 0, 0, len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]: 
                j += 1
            elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]: 
                return False
        return j == m
        
S = "heeellooo"
words = ["hello", "hi", "helloo"]
print(Solution().expressiveWords(S, words))
