#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:37:31 2019

@author: anirban-mac
"""

"""
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of 
the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
import collections

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        dd = collections.defaultdict(list)
        if not matrix: 
            return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                # starting indices from 1, hence i+j+1.
                dd[i+j+1].append(matrix[i][j]) 
        #print(dd)     
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in dd.keys():
            if k%2==1: dd[k].reverse()
            result += dd[k]
        print(dd)
        return result
        
matrix = [[3],[2]]
print(Solution().findDiagonalOrder(matrix))