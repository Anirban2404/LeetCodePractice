#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:51:30 2019

@author: anirban-mac
"""

"""
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five 
terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say 
sequence.

Note: Each term of the sequence of integers will be represented as a string.
Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            prev = res
            res = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1
                    j += 1
                res += str(cnt) + str(cur)
                print(res)
        return res

n = 4
print(Solution().countAndSay(n))