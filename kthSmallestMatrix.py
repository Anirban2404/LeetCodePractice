#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:22:24 2019

@author: anirban-mac
"""
"""
Given a n x n matrix where each of the rows and columns are sorted 
in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the 
kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""
class Solution:
    def kthSmallestNaive(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        order_arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                #print (matrix[i][j])
                order_arr.append(matrix[i][j])
        order_arr.sort()
        return (order_arr[k-1])
    
    def kthSmallest(self, matrix, k):

        lo, hi = matrix[0][0], matrix[-1][-1]
        N = len(matrix)
        
        while lo <= hi:
            mid = int((lo + hi)/2)
            print("mid", mid,hi,lo)
            col = N - 1
            count = 0
            for row in range(N):
                while col > -1 and matrix[row][col] > mid:
                    print(matrix[row][col])
                    col -= 1
                    print("co;:",col)
                count += col + 1
            print("c", count)
            if count >= k :
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        
 
            
    
matrix = [
   [ 1,  5,  9],
   [10, 11, 19],
   [12, 18, 199],
  ]
k = 8
print(Solution().kthSmallest(matrix,k))