#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:42:45 2019

@author: anirban-mac
"""

"""
777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a 
move consists of either replacing one occurrence of "XL" with "LX", or 
replacing one occurrence of "RX" with "XR". Given the starting string start 
and the ending string end, return True if and only if there exists a sequence 
of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s = [(x, i) for i, x in enumerate(start) if x != 'X']
        e = [(y, j) for j, y in enumerate(end) if y != 'X']
        
        if len(s) != len(e):
            return False
        for (x, i),(y, j) in zip(s,e):
            if x != y:
                return False
            if x == "L":
                if i < j:
                    return False
            if x == "R":
                if i > j:
                    return False
        return True
    
    
start = "RXXLRXRXL"
end = "XRLXXRRLX"
print(Solution().canTransform(start,end))