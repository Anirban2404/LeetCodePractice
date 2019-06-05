#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:08:39 2019

@author: anirban-mac
"""

"""
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        newIntervals = []
        for interval in intervals:
            interval = Interval(interval[0],interval[1])
            newIntervals.append(interval)
        
        # If there are no meetings, cannot attend any meeting.
        if not newIntervals:
            return True
        


        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i.start for i in newIntervals])
        end_timings = sorted(i.end for i in newIntervals)
        print(start_timings)
        print(end_timings)
        # Total number of Meetings
        L = len(newIntervals)
        print(L)
        if L == 1:
            return True
        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0
        
        while start_pointer < L:
            
            # If there is a meeting that has ended by the time the meeting at 
            #`start_pointer` starts
            start_pointer += 1  
            print(start_pointer, end_pointer)
            if start_timings[start_pointer] >= end_timings[end_pointer]: 
                end_pointer += 1  
            else:
                return False
            
            if start_pointer == L-1:
                return True
            
        return False
        
        
intervals = [[0,30],[5,10],[15,20]]
#intervals = [[7,10],[2,4]]

print(Solution().canAttendMeetings(intervals))