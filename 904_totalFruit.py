#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:09:23 2019

@author: anirban-mac
"""

"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.

2. Move to the next tree to the right of the current tree.  
If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: 
you must perform step 1, then step 2, then back to step 1, then step 2, 
and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, 
but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""
import collections

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        maxval = i = 0
        basket = collections.Counter()
        for j, fruit in enumerate(tree):
            basket[fruit] += 1
            print(basket)
            while len(basket) >= 3:
                basket[tree[i]] -= 1
                if basket[tree[i]] == 0:
                    del basket[tree[i]]
                i += 1
                print(basket,basket[tree[i]],i)
            maxval = max(maxval, j - i + 1)
            print(basket, maxval, i)
        return maxval
    
tree = [3,1,3,1,3,1,3,1,3,1,3,1,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(tree))