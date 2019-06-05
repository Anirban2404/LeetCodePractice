#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:09:37 2019

@author: anirban-mac
"""
"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

https://leetcode.com/problems/trapping-rain-water/
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
this case, 6 units of rain water (blue section) are being trapped. Thanks 
Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = right_max = area = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    area += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    area += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return area
                
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))