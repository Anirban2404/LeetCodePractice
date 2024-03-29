#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:38:08 2019

@author: anirban-mac
"""
"""
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and 
for the multiples of five output “Buzz”. For numbers which are multiples of 
both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzarr = []
        for i in range (1, n + 1):
            if i%15 == 0:
                #print ("FizzBuzz")
                fizzBuzzarr.append("FizzBuzz")
            elif i%3 == 0:
                #print("Fizz")
                fizzBuzzarr.append("Fizz")
            elif i% 5 == 0:
                #print("Buzz")
                fizzBuzzarr.append("Buzz")
            else:
                #print (i)
                fizzBuzzarr.append(str(i))
        return fizzBuzzarr
    
n = 15
print(Solution().fizzBuzz(n))