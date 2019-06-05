#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:38:25 2019

@author: anirban-mac
"""

"""
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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

    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        def pathSum(node):
            if node is None:
                return 0
            leftSum = max(pathSum(node.left), 0)
            rightSum = max(pathSum(node.right), 0)
            
            nodeSum = node.val + leftSum + rightSum
            self.max_sum = max(self.max_sum, nodeSum)
            return node.val + max(leftSum,rightSum)
        
        pathSum(root)
        return self.max_sum
        
treelist = [1,-2,-3,1,3,-2,'null',-1]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
print(Solution().maxPathSum(treeNode))