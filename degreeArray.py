#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:31:35 2019

Given a non-empty array of non-negative integers nums, the degree of this array 
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of
 nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

@author: anirban-mac
"""

class degreeArray:
    #def findShortestSubArray(self, nums: List[int]) -> int:
    def findShortestSubArray(self, nums):
        numdict = {}
        i = 0
        keyarr = []
        
        for i in nums:
            if i in numdict:
                numdict[i] = numdict[i] + 1
            else:
                numdict[i] = 1
        #print(numdict)
        
        degree = max(numdict.values())
        print(degree)

        for key, value in numdict.items(): 
            if value == degree:
                mykey = key
                #print("mykey", mykey)
                keyarr.append(mykey)
        
      
        print(keyarr)
        lenarr = []
        for i in keyarr:
            #print("arr: ", i)
            start = (nums.index(i))
            for num in range(len(nums)):
                if nums[num] == i:
                    #print(num, nums[num])
                    end = num
        
            lenarr.append(end - start + 1)
            #print("length: ",i,"-->", end - start + 1)
            
        #print(mykey,'-->',maxval)

        #print("length: ", min(lenarr))
        return min(lenarr)
    
#nums = [1,2,2,1,2,1,1,1,1,2,2,2]
#nums = [1,2,2,3,1]

nums = [1,2,2,3,1,4,2]
print(degreeArray().findShortestSubArray(nums))

"""
class Solution(object):
    def findShortestSubArray(self, nums):
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
"""