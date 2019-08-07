#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:16:45 2019

@author: anirban-mac
"""

"""
518. Coin Change 2
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
"""

class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for amt in range(1, amount + 1):
                if amt >= coin:
                    dp[amt] += dp[amt - coin]
        return dp[amount]

amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))