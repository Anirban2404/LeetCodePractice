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
    def searchMatrixNaive(self, matrix, target):
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
                
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        left, right = 0, len(matrix)*len(matrix[0])

        while left<right:
            mid = (int)((left+right)/2)
            i = (int)(mid/len(matrix[0]))
            j = (int)(mid%len(matrix[0]))

            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                right = mid
            else:
                left = mid + 1
    
        return False

matrix = matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 17],
   [14, 16, 18]
]
target = 16
print(Solution().searchMatrix(matrix,target))