#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:51:36 2019

@author: anirban-mac
"""

"""
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and 
some are not. However, flowers cannot be planted in adjacent plots - they would 
compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means 
empty and 1 means not empty), and a number n, return if n new flowers can be 
planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] ==0)\
                and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    flowerbed[i] == 1
                    count += 1
            if count >= n:
                return True
        return False
            
        
flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))