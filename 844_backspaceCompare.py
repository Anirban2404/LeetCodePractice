#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:54:43 2019

@author: anirban-mac
"""
"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
#        ans_s = ''
#        ans_t = ''
#        for i in S:
#            if i == '#':
#                ans_s = ans_s[:-1]
#            else:
#                ans_s += i
#        #print(ans_s)
#        for i in T:
#            if i == '#':
#                ans_t = ans_t[:-1]
#            else:
#                ans_t += i
#        return ans_s == ans_t
        
        lenS = len(S) - 1
        lenT = len(T) - 1
        skipS, skipT = 0, 0
        
       
        while True:
            while lenS >= 0 and (skipS or S[lenS] == '#'):
                skipS += 1 if S[lenS] == '#' else -1
                lenS -= 1
            while lenT >= 0 and (skipT or T[lenT] == '#'):
                skipT += 1 if T[lenT] == '#' else -1
                lenT -= 1
            if not (lenS >= 0 and lenT >= 0 and S[lenS] == T[lenT]):
                return lenS == lenT == -1
            lenS, lenT = lenS - 1, lenT - 1
        return True
                 
              
    
S = "ab##" 
T = "#c#d"
print(Solution().backspaceCompare(S,T))