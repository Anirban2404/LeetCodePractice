#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:47:52 2019

@author: anirban-mac
"""

class Solution:
    def generalizedGCD(self, num, arr):
        # WRITE YOUR CODE HERE
        if num == 1:
            return arr[0]

        num1 = arr[0]
        num2 = arr[1]
        gcd = self.find_gcd(num1,num2)
        
        
        for i in range(2, num):
            gcd = self.find_gcd(gcd, arr[i])
        return gcd
        
    def find_gcd(self, x,y):
        while y:
            x, y = y, x % y
        return x

num = 4
arr = [2,3,4,5]
print(Solution().generalizedGCD(num,arr))