#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:30:06 2019

@author: anirban-mac
"""

"""
Given a string, find the first non-repeating character in it and return 
it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
import collections
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        slist = list(s)
        sdict = {}
        count = 1
        
        for i in range(len(slist)):
#            print(sdict.keys())
            if slist[i] not in sdict.keys():
#                print(sdict.keys())
                sdict[slist[i]] = count
#                print(sdict[slist[i]])
            else:
                sdict[slist[i]] = sdict[slist[i]] + 1
                
#        print(sdict)
        for i,v in sdict.items():
#            print(i,v)
            if v==1:
                return(s.index(i))
        
        return(-1)
        
    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1       
        return -1

        
s = "leetcode"
print(Solution().firstUniqChar2(s))