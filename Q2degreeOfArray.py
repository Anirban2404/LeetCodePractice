#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 13:33:16 2019

@author: anirban-mac
"""

"""
Q2 Degree of an Array

Given an array of n integers, we define its degree as the maximum frequency of 
any element in the array. For example, the array [1,2,2,4,3,3,2] has a degree of  
3 because the number 2 occurs three times (which is more than any other number 
in the array). We want to know the size of the smallest subarray of our 
array such that the subarray's degree is equal to the array's degree. 

Complete the function in the editor below. It has one parameter: an array of n 
integers, arr. The function must return an integer denoting the minimum size 
of the subarray such that the degree of the subarray is equal to the degree of
the array.

Sample Input 0

5
1
2
2
3
1
Sample Output 0

2
"""

#!/bin/python3

import sys
from collections import Counter

def degreeOfArray(arr):
    # Complete this function
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left: left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    return ans
    
    
if __name__ == "__main__":
    size = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(size):
    	arr_t = int(input().strip())
    	arr.append(arr_t)
    res = degreeOfArray(arr)