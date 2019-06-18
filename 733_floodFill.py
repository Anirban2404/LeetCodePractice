#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:37:31 2019

@author: anirban-mac
"""

"""
733. Flood Fill
An image is represented by a 2-D array of integers, each integer representing 
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of 
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color as the 
starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color as the starting pixel), and so on. Replace the color 
of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels 
connected  by a path of the same color as the starting pixel are colored with 
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally 
connected to the starting pixel.
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        if image is None or len(image) < 1:
            return []
        nrows = len(image)
        ncols = len(image[0])
        print(nrows, ncols)
        cur_color = image[sr][sc] 
        if cur_color == newColor:
                return image
            
        def dfs(image, i, j):
            if i < 0 or j < 0 or i >= nrows or j >= ncols:
                return
            
            if image[i][j] == cur_color:
                image[i][j] = newColor
                dfs(image, i+1, j)
                dfs(image, i-1, j)
                dfs(image, i, j+1)
                dfs(image, i, j-1)
                
            
        dfs(image, sr, sc)
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))