#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:03:54 2019

@author: anirban-mac
"""

class Solution:
    def factorial(self, n):
        fact = 1
        if n == 0 or n == 1:
            return fact
#        for i in range(2,n+1):
#            fact = fact * i
#        return fact
        
        #print(self.factorial(n-1))
        fact = n * self.factorial(n-1)
        return fact 
    
n = 4
print(Solution().factorial(n))