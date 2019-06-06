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

        maxprofit = 0
        minprice = float('inf')
        for i in range(0, len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice;
        
        return maxprofit;
            
        
prices = [7,1,5,3,6,4]
#print(Solution().maxProfit(prices))
print(Solution().maxProfit2(prices))