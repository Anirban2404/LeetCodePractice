#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:57:00 2019

@author: anirban-mac
"""

"""
409. Longest Palindrome


Given a string which consists of lowercase or uppercase letters, find the length 
of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections 

class Solution:
    
    def longestPalindrome(self, s):
        if len(s) < 1:
            return 0
        letterCounter = {}
        for letter in s:
            if letter in letterCounter:
                letterCounter[letter] += 1
            else:
                letterCounter[letter] = 1
        #print(letterCounter)
        sum = 0
        ones = False
        for key, value in letterCounter.items():
            #print (key, value)
            if value % 2 == 0:
                sum = sum + value
            elif value % 2 != 0:
                sum = sum + value - 1
                ones = True
        if ones:
            sum = sum + 1
        return sum
      
        """
       def longestPalindrome(self, s):
           ans = 0
           for v in collections.Counter(s).values():
               ans += v // 2 * 2
               if ans % 2 == 0 and v % 2 == 1:
                   ans += 1
           return ans         
       """ 
s = "abccccdd"
print(Solution().longestPalindrome(s))