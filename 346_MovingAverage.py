#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:12:48 2019

@author: anirban-mac
"""

"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        #print(len(self.q))
        if len(self.q) >= self.size:
            self.q.pop()
        self.q.appendleft(val)
        return (float(sum(self.q))/len(self.q))
        
        


# Your MovingAverage object will be instantiated and called as such:
size = 2
m = MovingAverage(size)
print(m.next(1))
print(m.next(4))
print(m.next(0))