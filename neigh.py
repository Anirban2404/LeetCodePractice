#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:41:50 2019

@author: anirban-mac
"""
"""
https://www.interviewbit.com/problems/neigh/
In real world horses neigh, and you can count them by listening to them.

For this problem you will be given an input string consisting of lowercases 
letters which represents combination of neigh of different horses.

You need to return an integer corresponding to minimum number of distinct horses 
which can produce the given sequence.

If the input string is not a combination of valid neigh from different horses 
return -1.

Example :

Input : "nei"
Output : -1
Explanation: Not a valid neigh.
Input : "neighneigh"
Output : 1
Explanation: Single horse yelling neigh two times.
Input : "neingeighh"
Output : 2
Explanation: Second horse can be seen speaking before the first one finished.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solveneigh(self, A):
        word = "neigh"
        charDict = {val: key for key,val in enumerate(word)}
        print(charDict)
        dp = [0] * (len(word))
        maxC = curC = 0
        
        #Invalid Cases
        if len(A) % len(word) != 0 or A[0] != word[0]:
            return -1
        
        for i in range(len(A)):
            #print(A[i])
            if A[i] not in charDict:
                return -1
            idx = charDict[A[i]]
            print(dp, idx)
            if idx == 0:
                curC += 1
                maxC = max(maxC, curC)
                dp[0] += 1
            else:
                if (dp[idx - 1] == 0):
                    return -1
                dp[idx - 1] -= 1
                if idx == len(word) - 1:
                    curC -= 1
                else:
                    dp[idx] += 1 
        print(dp, idx)  
        return maxC

        
A = "neigneihgh"
print(Solution().solveneigh(A))