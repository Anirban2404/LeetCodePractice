#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:10:01 2019

@author: anirban-mac
"""

"""
95. Unique Binary Search Trees II
Given n, how many structurally unique BST's (binary search trees) that store 
values 1 ... n?
Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)
                
                for l in left:
                    for r in right:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            return all_trees
        return generate(1, n) if n else []
    
    def prettyPrintTree(self, node, prefix="", isLeft=True):
        if not node:
            print("Empty Tree")
            return
    
        if node.right:
            self.prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)
    
        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))
    
        if node.left:
            self.prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)



n = 3
treeNodes = Solution().generateTrees(n)
for treeNode in treeNodes:
    Solution().prettyPrintTree(treeNode,"",True)