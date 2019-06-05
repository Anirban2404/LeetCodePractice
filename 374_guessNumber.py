#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:35:54 2019

@author: anirban-mac
"""
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results 
(-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #for i in range(n):
        #   if self.guess(i) ==  0:
        #      return i
        start = 0
        end = n 
        
        while start <= end:
            mid = (start + end)//2
            print(mid, start, end, self.guess(mid))
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == -1:
                start = mid + 1
            else:
                end =mid - 1
        
        
    def guess(self, n):
        pick = 6
        print (n)
        if n == pick:
            return 0
        elif n > pick:
            return 1
        else:
            return -1
        
n = 10
pick = 10
print(Solution().guessNumber(n))