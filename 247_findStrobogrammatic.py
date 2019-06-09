#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:15:12 2019

@author: anirban-mac
"""

"""
247. Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 
degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        self.helper(result, [None]*n, 0, n-1, dic)

        return result

    def helper(self, result, item, start, end, dic):
        if start > end:
            result.append(''.join(item))
            return
        print(item, start, end)
        for key in dic:
            if start == end and key in ('6','9'):
                continue

            if start != end and start == 0 and key == '0':
                continue

            item[start], item[end] = key, dic[key]
            #print(item)
            self.helper(result, item, start+1, end-1, dic)
        return
    
n = 3
print(Solution().findStrobogrammatic(n))