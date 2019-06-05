#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:33:05 2019

@author: anirban-mac
"""

"""
Given two strings A and B, find the minimum number of times A has to be 
repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a 
substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        q = (len(B) - 1) // len(A) + 1
        #print(q)
        #print(A * (q+1))
        for i in range(2):
            if B in A * (q+i): 
                return q+i
        return -1
        
        
A = "abcd"
B = "cdabcdabcdabcdab"
print(Solution().repeatedStringMatch(A,B))