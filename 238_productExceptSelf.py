#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:09:25 2019

@author: anirban-mac
"""

"""

238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not 
count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """
        products = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                 if i == j:
                     continue
                 else:
                    print(nums[i], nums[j])
                    product = product * nums[j]
            print(product)
            products.append(product)
        return products
        """
        
        product = 1
        products = []
        for num in nums:
            products.append(product)
            product = product * num
            print(product)
        print(products)
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            print(nums[i], products[i], product)
            products[i] = products[i] * product
            product = product * nums[i]
            
        return (products)
        
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))