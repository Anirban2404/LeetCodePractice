#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:48:44 2019

@author: anirban-mac
"""

"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example, given a 3-ary tree:

 



 

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        if root is None:
            return levels
        level = 0
        q = deque([root])
        
        while q:
            levels.append([])
            for i in range(len(q)):
                
                root = q.popleft()
                levels[level].append(root.val)
                if root.children:
                    for child in root.children:
                        q.append(child)
                    
            level += 1
        return levels
            
    def levelOrder2(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        levels = []
        level = 0
        
        if root is None:
            return levels
        
        def helper(node, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            for child in node.children:
                helper(child, level+1)
        helper(root,0)
        return levels
    
