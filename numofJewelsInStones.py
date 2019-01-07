#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:03:36 2019

@author: anirban-mac
"""
"""
You're given strings J representing the types of stones that are jewels, and S 
representing the stones you have.  Each character in S is a type of stone you 
have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are 
letters. Letters are case sensitive, so "a" is considered a different type of 
stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0  
         
        for stone in S:
            print(stone)
            
            if stone in J:
                count = count +1
        print(count)
        return count
J = "z"
S = "zZZ"

print(Solution().numJewelsInStones(J,S))        