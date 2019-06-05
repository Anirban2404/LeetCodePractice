#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:01:49 2019

@author: anirban-mac
"""

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can 
you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    
    """
    def climbStairs(self, n):
        return self.climb_Stairs(0,n)
       
    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        else:
            return(self.climb_Stairs( i + 1, n) + self.climb_Stairs( i + 2, n))
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3,n+1):
            #third = first + second
            #first = second
            #second = third
            first, second = second, first + second
        return second
    
n = 5
print(Solution().climbStairs(n))