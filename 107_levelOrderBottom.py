#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:18:14 2019

@author: anirban-mac
"""

"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root is None:
            return None
        queue = deque([root])
        level = 0
        while queue:
            levels.append([])
            for i in range(len(queue)):
                root = queue.popleft()
                levels[level].append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level += 1
        return levels[::-1]
        
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

treelist = [3,9,20,15,7,2]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
print(Solution().levelOrderBottom(treeNode))