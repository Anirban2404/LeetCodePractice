#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:49:25 2019

@author: anirban-mac
"""

"""
11.Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point 
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#        maxval = 0
#        for i in range(len(height) - 1):
#            for j in range(i+1, len(height)):
#                area = min(height[i],height[j]) * (j-i)
#                print(area,"-->(",height[i],height[j], ")-->",j,i)
#                maxval = max(maxval,area)
#        return maxval
        maxarea = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            area = min(height[left],height[right]) * (right - left)
            maxarea = max(maxarea,area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxarea
    
height = [1,8,6,2,5,100,150,4,8,3,7]
print(Solution().maxArea(height))