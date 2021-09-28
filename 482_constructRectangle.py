#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:25:59 2019

@author: anirban-mac
"""

"""
492. Construct the Rectangle

For a web developer, it is very important to know how to design a web page's 
size. So, given a specific rectangular web page’s area, your job by now is to 
design a rectangular web page, whose length L and width W satisfy the following 
requirements:

1. The area of the rectangular web page you designed must equal to the given 
target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in 
sequence.

Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it 
are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  
[4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W 
is 2.
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 0:
            return []
        W = 1
        L = area
        while L >= W:
            mid = (L + W)//2
            if area /(mid * mid) == 1:
                return (mid,mid)
            elif area > (mid * mid):
                W = mid + 1
            else:
                L = mid - 1
            print(L,W)
        sqrt = (L + W) // 2
        for W in range(sqrt, 0, -1):
            if area%W == 0:
                L = area/W
                break
        return(int(L),W)

area = 5
print(Solution().constructRectangle(area))