#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:42:21 2019

@author: anirban-mac
"""
"""
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the 
Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above 
it.

Example:

Input: 3
Output: [1,3,3,1]
"""
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        
        for row in range(0, rowIndex + 1):
            #print (rowIndex)
            numerator = self.factorial(rowIndex)  
            #print(numerator)
            denominator = self.factorial(row) * self.factorial(rowIndex - row)
            #print(denominator)
            result = numerator//denominator
            triangle.append(result)
            #print(result)
        return triangle
        
    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num - 1)
        
    
rowIndex = 0
print (Solution().getRow(rowIndex))