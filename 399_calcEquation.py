#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:30:39 2019

@author: anirban-mac
"""

"""
399. Evaluate Division
Equations are given in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, 
vector<pair<string, string>> queries , where equations.size() == values.size(), 
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will 
result in no division by zero and there is no contradiction.
"""

from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def dfs (start, end, path, paths):
            if start == end and start in G:
                paths[0] = path
                return 
            if start in vis:
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path * W[start, node], paths)
            
        G = defaultdict(set)
        W = defaultdict(float)
        for (A, B), V in zip(equations , values):
            G[A] , G[B] = G[A] | {B}, G[B] | {A}
            W[A,B] , W[B,A] = V, 1.0 / V
        res = []
        for x,y in queries:
            paths, vis = [-1.0], set()
            dfs(x, y, 1.0, paths)
            res += paths[0],
        return res
            
            
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))