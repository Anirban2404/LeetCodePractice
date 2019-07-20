#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:30:09 2019

@author: anirban-mac
"""

"""
Say you have an array for which the ith element is the price of a given stock 
on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to 
find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

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

        maxprice = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if maxprice < profit : 
                    maxprice = profit
        return (maxprice)
        
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price_local = float('-inf')
        max_profit_local, max_profit = 0, 0
    
        for price in prices:
            min_price_local = min(min_price_local, price)
            max_profit_local = max(max_profit_local, price - min_price_local)
            max_profit = max(max_profit, max_profit_local)
       
        return max_profit
            
        
prices = [7,1,5,3,6,4]
#print(Solution().maxProfit(prices))
print(Solution().maxProfit2(prices))