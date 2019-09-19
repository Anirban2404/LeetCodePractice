#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:16:48 2019

@author: anirban-mac
"""

"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list 
is even, there is no middle value. So the median is the mean of the two middle 
value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data 
structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
import heapq 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
#obj.addNum(2)
#
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
med2 = obj.findMedian()
print(med2)

#commands = ["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
#variables = [[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]]
#
#for command,var in zip(commands,variables):
#    if len(var) != 0:
#        num = var[0]
#        cmd = "obj." + command + "(num)"
#    else:
#        cmd = "obj." + command + "(" + ")"
#    #print(cmd)
#    res = (exec(cmd))
#    #print(res)
#        

    