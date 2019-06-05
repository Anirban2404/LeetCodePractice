#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:42:23 2019

@author: anirban-mac
"""

"""
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms 
required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        newIntervals = []
        for interval in intervals:
            #print (interval)
            interval = Interval(interval[0],interval[1])
            newIntervals.append(interval)
            #print (interval.start, interval.end)
        # If there is no meeting to schedule then no room needs to be allocated.
        # If there are no meetings, we don't need any rooms.
        if not newIntervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i.start for i in newIntervals])
        end_timings = sorted(i.end for i in newIntervals)
        L = len(newIntervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at 
            #`start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any 
            #effect. used_rooms would
            # remain the same in that case. If no room was free, then this would
            #increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
    
intervals = [[0,30],[5,10],[15,20]]
print(Solution().minMeetingRooms(intervals))