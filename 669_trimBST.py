#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:18:11 2019

@author: anirban-mac
"""

"""
669. Trim a Binary Search Tree

Given a binary search tree and the lowest and highest boundaries as L and R, 
trim the tree so that all its elements lies in [L, R] (R >= L). You might need 
to change the root of the tree, so the result should return the new root of 
the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
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


    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)
        
treelist = [3,9,20,15,7,2]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
L = 3
R = 16
trimmedNode = Solution().trimBST(treeNode, L, R)
#print(trimmedNode)
Solution().prettyPrintTree(trimmedNode,"",True)