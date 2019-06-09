#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:25:36 2019

@author: anirban-mac
"""

"""
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedList = []
        output = [0] * len(nums)
        
        for i in range(len(nums)):
            left, right = 0, len(sortedList) - 1
            idx = len(nums) - 1 - i
            while left <= right:
                mid = left + (right - left) // 2
                if sortedList[mid] < nums[idx]:
                    left = mid + 1
                else:
                    right = mid - 1
            sortedList.insert(left, nums[idx])
            print(sortedList)
            print(output)
            output[idx] = left
        return output
        
        
        

nums = [5,2,6,2,1]
print(Solution().countSmaller(nums))