#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:32:11 2019

@author: anirban-mac
"""

"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return 
the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levels = []
        res = []
        if root is None:
            return levels
        q = deque([root])
        level = 0
        while q:
            levels.append([])
            for _ in range(len(q)):
                root = q.popleft()
                levels[level].append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            res.append(levels[level][-1])
            level += 1
        
        return res
        
    def stringToTreeNode(self,inputValues):
      
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1
    
            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)
    
            if index >= len(inputValues):
                break
    
            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root


    def prettyPrintTree(self, node, prefix="", isLeft=True):
        if not node:
            print("Empty Tree")
            return
    
        if node.right:
            self.prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)
    
        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))
    
        if node.left:
            self.prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

treelist = [1,2,3,'null',5,'null',4]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
print(Solution().rightSideView(treeNode))