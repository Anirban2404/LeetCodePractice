#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:23:21 2019

@author: anirban-mac
"""

"""
506. Relative Ranks
Given scores of N athletes, find their relative ranks and the people with the 
top three highest scores, who will be awarded medals: "Gold Medal", "Silver 
Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they
 got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks 
according to their scores.
"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        s = {n: i for i, n in enumerate(sorted(nums, reverse=True))}
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        
        res = []
        for num in nums:
            if s[num] >= len(medals) : 
                res.append(str(s[num]+1))
            else:
                res.append(medals[s[num]])
        return res
        
nums = [10,3,8,9,4]
print(Solution().findRelativeRanks(nums))