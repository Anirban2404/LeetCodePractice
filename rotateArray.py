#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:22:03 2019

@author: anirban-mac
"""
"""
Given an array, rotate the array to the right by k steps, where k is 
non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different 
ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if len(nums) == 1 or len(nums) == 0:
            pass
        else:
            for i in range(k):
                temp = nums[0]
                nums[0] = nums[length-1]
                for j in range(len(nums)-2,-1,-1):
                    nums[j+1] = nums[j]
                nums[1] = temp
        print(nums)   
        
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        if length == 1 or length == 0:
            pass
        else:
            k = k % length
            nums[:] = nums[length-k:] + nums[:length-k] 
        print(nums)
    
    def reverse(self, nums, start, end):
        
        i = start
        #print("1:", nums)
        while end > start:
            #print(i)
            temp = nums[end] 
            nums[end] = nums[start]
            nums[start] = temp
            i = i + 1
            end = end - 1
            start = start + 1
        #print("2:", nums)
        
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        if length == 1 or length == 0:
            pass
        else:
            k = k % length
            Solution().reverse(nums,0,length-1) 
            Solution().reverse(nums,0,k-1)
            Solution().reverse(nums,k,length-1 ) 
        print(nums)
        
nums = [1,2,3,4,5,6,7]
k = 3
#print(Solution().rotate1(nums,k))
#print(Solution().rotate2(nums,k))
print(Solution().rotate3(nums,k))
