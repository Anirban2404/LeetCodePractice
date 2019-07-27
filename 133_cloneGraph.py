#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:43:09 2019

@author: anirban-mac
"""
"""
133. Clone Graph
Given a reference of a node in a connected undirected graph, return a deep copy 
(clone) of the graph. Each node in the graph contains a val (int) and a list 
(List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3",
"neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],
"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs (input, check):
            if input in check:
                return check[input]
            
                  
            new_node = Node(input.val, [])
            check[input] = new_node
            for neighbor in input.neighbors:
                new_node.neighbors.append(dfs(neighbor, check))
            return new_node 
        if node is None:
            return None
        return dfs(node, {})

#print(Solution().cloneGraph(node))