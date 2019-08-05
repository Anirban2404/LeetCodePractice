#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:06:40 2019

@author: anirban-mac
"""
"""
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        col_zer0 = False
        for i in range(nrows):
            if matrix[i][0] == 0:
                col_zer0 = True
            for j in range(1, ncols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, nrows):
            for j in range(1, ncols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(ncols):
                matrix[0][j] = 0

        if col_zer0:
            for i in range(nrows):
                matrix[i][0] = 0
                
        return matrix
    
matrix = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(Solution().setZeroes(matrix))