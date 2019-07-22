#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:54:24 2019

@author: anirban-mac
"""

"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where 
the width of each bar is 1, find the area of largest rectangle in the histogram.
https://leetcode.com/problems/largest-rectangle-in-histogram/
 

Example:

Input: [2,1,5,6,2,3]
Output: 10

"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
#        maxArea = 0
#        area = 0
#        
#        for i in range(len(heights)):
#            minHeight = float('inf')
#            for j in range(i, len(heights)):
#                minHeight = min(minHeight, heights[j]) 
#                area = minHeight * (j + 1 - i)
#                maxArea = max(maxArea, area)
#                
#        return maxArea
        stack = []
        maxArea = 0
        idx = 0
        while idx < len(heights):
            if (not stack) or heights[stack[-1]] <= heights[idx]:
                stack.append(idx)
                idx += 1
            else:
                top = stack.pop(-1)
                area = (heights[top] * ((idx - stack[-1] - 1)\
                            if stack else idx))
                maxArea = max(maxArea, area)
        
        while stack:
            top = stack.pop(-1)
            area = (heights[top] * ((idx - stack[-1] - 1)\
                        if stack else idx))
            maxArea = max(maxArea, area)
        
        return maxArea

heights = [0]
print(Solution().largestRectangleArea(heights))