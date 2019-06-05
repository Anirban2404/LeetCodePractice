#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:49:46 2019

@author: anirban-mac
"""
"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two 
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add 
up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not 
use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """


        for i,num in enumerate(numbers):
            complement = target - num
            """
            if complement in numbers[i+1:]:
                print(numbers[i+1:], i)
                if complement < num:
                    continue
                return i + 1, numbers[i+1:].index(complement) + i + 2
            """
            if self.binarySearch(numbers[i+1:],complement):
                return i + 1, numbers[i+1:].index(complement) + i + 2
        return -1, -1
                
    def binarySearch(self, nums, complement):
        start = 0
        end = len(nums) - 1
        while (start<=end):
             mid = int(start + (end - start)/2)
             if nums[mid]>complement:
                 end = mid - 1
             elif nums[mid]<complement:
                 start = mid + 1
             else:
                 return True
        return False
       
            
#numbers = [2,7,11,15]
numbers = [0,0,3,4,5]

target = 5
print(Solution().twoSum(numbers,target))
#print(Solution().binarySearch(numbers,target))