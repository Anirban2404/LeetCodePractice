#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:14:28 2021

@author: anirban-mac
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        _maxCount = 0
        _count = 0
        _skipCount = 0
        _skip = True
        
        for num in nums:
            if num == 1:
                _count += 1
                
            else:
                if _skip: 
                    _skip = False
                    _skipCount = _count
                    _count += 1
                else: 
                    _count = _count - _skipCount - 1
                    _skipCount = _count 
                    
                    _count += 1
            _maxCount = max(_maxCount, _count)
            print(_skipCount, _count, _maxCount)
        return _maxCount
    
nums = [1,0,1,1,0,0,1,1,1,1,0]
print(Solution().findMaxConsecutiveOnes(nums))