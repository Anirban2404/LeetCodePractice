#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:00:52 2019

@author: anirban-mac
"""

"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible 
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding 
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

1. Find the largest index k such that nums[k] < nums[k + 1]. 
If no such index exists, just reverse nums and done.
2. Find the largest index l > k such that nums[k] < nums[l].
3. Swap nums[k] and nums[l].
4. Reverse the sub-array nums[k + 1:].


"""
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        candidate = 0
        index = -1
        #Find the largest index k such that nums[k] < nums[k + 1].
        for i in range(len(nums)-1,-1,-1):
            #print(nums[i],nums[i-1])
            if nums[i] > nums[i-1]:
                candidate = (nums[i-1])
                index = i - 1
                break
        # If no such index exists, just reverse nums and done.
        if index == -1 :
            #Reverse All
            return self.reverse(nums, index, len(nums)-1)
        maxcount = index+1
        
        #Find the largest index l > k such that nums[k] < nums[l].
        for i in range(index+1, len(nums)):            
            if candidate < nums[i]:
                maxcount = max(maxcount,i)

        #Swap nums[k] and nums[l].
        nums[index], nums[maxcount] = nums[maxcount], nums[index]
        print(nums)
        # Reverse the sub-array nums[k + 1:].
        self.reverse(nums, index, len(nums)-1)
        print(nums)
        
    def reverse(self, nums, start, end):
        index = start
        while index < end:
            nums[index + 1], nums[end] = nums[end], nums[index + 1]
            index += 1
            end -= 1
        return (nums)
        
nums = [1,5,8,4,5,5,5,5,5,4] #1,5,8,5,1,3,4,6,7
#nums = [1,2,3]
#nums = [1,3,2]
print(Solution().nextPermutation(nums))