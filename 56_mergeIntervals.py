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
           
        newIntervals = []
        for interval in intervals:
            #print (interval)
            interval = Interval(interval[0],interval[1])
            newIntervals.append(interval)
        
        if not newIntervals:
            return None
        
        newIntervals.sort(key = lambda x: x.start)
        merged = []

        for interval in newIntervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        
        ret = []
        for merge in merged:
            ret.append([merge.start, merge.end])
        return ret
        
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))