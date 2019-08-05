#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:22:14 2019

@author: anirban-mac
"""
"""
59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(matrix)
        if n == 0:
            return matrix
        
        rstart = 0
        rend = n - 1
        cstart = 0
        cend = n - 1
        count = 0
        
        while rstart <= rend and cstart <= cend:  
            
            for row in range(rstart, rend + 1):
                count += 1
                print("1", cstart, row, count) 
                matrix[cstart][row] = count
            cstart += 1
            print(matrix)
            
            for col in range(cstart, cend + 1):
                count += 1
                print("2", col, rend, count)
                matrix[col][rend] = count
            rend -= 1
            
            if rstart <= rend and cstart <= cend:
                for row in range(rend, rstart - 1, -1):
                    count += 1
                    print("3", cend, row, count)
                    matrix[cend][row] = count
                cend -= 1
                 
                for col in range(cend, cstart - 1, -1):
                    count += 1
                    print("4", col, cstart, count)  
                    matrix[col][rstart] = count
                rstart += 1
            #print (hstart, hend, vstart, vend)
        return matrix

n = 4
print(Solution().generateMatrix(n))