#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:38:47 2019

@author: anirban-mac
"""
"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the 
previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        print(len(matrix))
        if len(matrix) == 0:
            return False
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print("::", matrix[row][col])
                
                if matrix[row][col] == target:
                    return True

        return False
                
matrix = [[]]
target = 1
print(Solution().searchMatrix(matrix,target))