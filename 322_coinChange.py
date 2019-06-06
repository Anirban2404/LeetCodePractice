#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:17:21 2019

@author: anirban-mac
"""

"""
322. Coin Change
You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you need 
to make up that amount. If that amount of money cannot be made up by any 
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0
        
        dp = [2147483647 for _ in range(amount+1)]
        dp[0] = -1
      
        
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i and dp[i-c] >= -1:
                    dp[i] = min(dp[i], dp[i-c]+1)
            print(dp)
        return dp[amount] + 1 if dp[amount] < amount else -1
    

coins = [1, 2, 5]
amount =  11
print(Solution().coinChange(coins, amount))