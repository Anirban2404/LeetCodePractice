#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:10:15 2019

@author: anirban-mac
"""

"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents 
that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the 
closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has 
distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
      
#        people = (i for i, seat in enumerate(seats) if seat)
#        print(people)
#        prev, future = None, next(people)
#        
#        ans = 0
#        for i, seat in enumerate(seats):
#            if seat:
#                prev = i
#            else:
#                while future is not None and future < i:
#                    future = next(people, None)
#
#                left = float('inf') if prev is None else i - prev
#                right = float('inf') if future is None else future - i
#                ans = max(ans, min(left, right))
#
#        return ans
        prev = -1
        future = 0
        mingap = gap = 0
        L = len(seats)
        for i in range(L):
            if seats[i] == 1:
                prev = i
            else:
                while future < L and (seats[future] == 0 or future < i):
                    future += 1
                left = float('inf') if prev == -1 else i - prev
                right = float('inf') if future == L  else future - i
                gap = min(left, right)
                mingap = max(mingap, gap)
              
        return mingap
        
seats = [1,0,0,0]
print(Solution().maxDistToClosest(seats))