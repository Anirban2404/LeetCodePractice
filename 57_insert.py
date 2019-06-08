#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:15:29 2019

@author: anirban-mac
"""

"""
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the 
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their 
start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution:
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return list(newInterval)
        if len(newInterval) == 0:
            return intervals
        newIntervals = []
        
        for interval in intervals:
            #print (interval)
            interval = Interval(interval[0],interval[1])
            newIntervals.append(interval)
            
        newIntervals.append(Interval(newInterval[0],newInterval[1]))
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
                
        
        
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals,newInterval))