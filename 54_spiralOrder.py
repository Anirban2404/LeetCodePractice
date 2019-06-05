#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:25:33 2019

@author: anirban-mac
"""

"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of 
the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        spiralarr = []
        n = len(matrix)

        if n == 0:
            return spiralarr
        if n == 1:
            return matrix[0]

        m = len(matrix[0])
        """
        if m == 1:
            for i in range(n):
                spiralarr.append(matrix[i][0])
            return spiralarr
        """
        
        rstart = 0
        rend = m - 1
        cstart = 0
        cend = n - 1
            
        while rstart <= rend and cstart <= cend:        
            for row in range(rstart, rend + 1):
                print("1", matrix[cstart][row])
                spiralarr.append(matrix[cstart][row]) 
            cstart += 1
            
            for col in range(cstart, cend + 1):
                print("2",matrix[col][rend])
                spiralarr.append(matrix[col][rend]) 
            rend -= 1
            
            if rstart <= rend and cstart <= cend:
                for row in range(rend, rstart - 1, -1):
                    print("3",matrix[cend][row])
                    spiralarr.append(matrix[cend][row])
                cend -= 1
                 
                for col in range(cend, cstart - 1, -1):
                    print("4",matrix[col][rstart])
                    spiralarr.append(matrix[col][rstart])     
                rstart += 1
            #print (hstart, hend, vstart, vend)
        return spiralarr
        
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
"""
matrix = [[1,2],
          [3,4]]
"""

"""
matrix = [[1],
          [2],
          [3]]
"""

print(Solution().spiralOrder(matrix))