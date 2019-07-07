#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:33:42 2019

@author: anirban-mac
"""

"""
829. Consecutive Numbers Sum
Given a positive integer N, how many ways can we write it as a sum of 
consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
"""
import math
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        ans = 1
        for i in range(2, int(math.sqrt(2 * N))+1):
            if i % 2 and not N % i:
                ans += 1
            elif N / i - N // i == 0.5:
                ans += 1
        return ans
            

N = 15
print(Solution().consecutiveNumbersSum(N))