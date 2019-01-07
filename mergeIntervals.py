#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:01:08 2019

@author: anirban-mac
"""
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
#        merged_intervals = []
        
#        for interval in range(1,len(intervals)):
#            print(intervals[interval])
#            start = (intervals[interval][0])
#            end = (intervals[interval - 1][1])
#            print(start)
#            print(end)
#            if end >= start:
#                newList = [intervals[interval - 1][0],intervals[interval][1]]
#                print(newList)
#                merged_intervals.append(newList)
#            else:
#                merged_intervals.append(intervals[interval])
#        return(merged_intervals)   
        
        
        
intervals = Interval[[1,4],[4,5]]
print(Solution().merge(intervals))