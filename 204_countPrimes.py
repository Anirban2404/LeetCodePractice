#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:58:36 2019

@author: anirban-mac
"""

"""
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        primes = [True] * (n+1)
        count = 0
        
        for p in range(2, n):
            if primes[p]:
                count += 1
                for i in range(p * p, n + 1, p):
                    primes[i] = False
        return count
        
n = 1000
print(Solution().countPrimes(n))