#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:15:08 2019

@author: anirban-mac
"""

"""
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = [0] * len(prices)
        min_price = float('inf')
        maxProfit_local = 0
        
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            maxProfit_local = max(maxProfit_local, price - min_price)
            maxProfit[i] = maxProfit_local
        print(maxProfit)
        
       
        max_price = float('-inf')
        for i, price in reversed(list(enumerate(prices[1:], 1))):
            #print(price)
            max_price = max(max_price, price)
            maxProfit_local = max(maxProfit_local,
                                  max_price - price + maxProfit[i - 1])
        return (maxProfit_local)
        
prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))