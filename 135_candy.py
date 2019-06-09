#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:37:49 2019

@author: anirban-mac
"""

"""
135. Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 
candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 
candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        L = len(ratings)
        candies = [1] * L
        
        for i in range(1, L):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i-1] + 1
       
        for i in range(L - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
            
        return sum(candies)
    
ratings = [1, 2, 2]
print(Solution().candy(ratings))