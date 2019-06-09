#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:15:36 2019

@author: anirban-mac
"""

"""
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you 
can split the array into m non-empty continuous subarrays. Write an algorithm 
to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
from collections import defaultdict
class Solution:
#    def splitArray(self, nums, m):
#        """
#        :type nums: List[int]
#        :type m: int
#        :rtype: int
#        """        
#        cache = defaultdict(dict)
#        return self.helper(0, nums, m, cache)
#    
#    def helper(self,i, nums, m, cache):
#        if len(nums) == 0:
#            return 0
#        elif m <= 1:
#            return sum(nums[i:])
#        else:
#            if i in cache and m in cache[i]:
#                return cache[i][m]
#            cache[i][m] = float('inf')
#            for j in range(1, len(nums) + 1):
#                left, right = sum(nums[i:i+j]), self.helper(i+j, nums, m-1, cache)
#                cache[i][m] = min(cache[i][m], max(left, right))
#                if left > right:
#                    break
#        print(cache)
#        return cache[i][m]
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """        
        low = max(nums)
        high = sum(nums)
        res = -1
        
        while(low <= high):
            mid = (low + high) // 2
            
            if self.isValid(nums, m, mid):
                res, high = mid, mid - 1
            else:
                low = mid + 1
        return res
        
    def isValid(self, nums, m, mid):
        cuts, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cuts += 1
                curr_sum = num
        return cuts + 1 <= m 
        
        
nums = [7,2,5,10,8]
m = 3
print(Solution().splitArray(nums, m))