#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:23:44 2019

@author: anirban-mac
"""
"""
701. Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted 
into the tree, insert the value into the BST. Return the root node of the BST 
after the insertion. It is guaranteed that the new value does not exist in the 
original BST.

Note that there may exist multiple valid ways for the insertion, as long as the 
tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

"""

#Definition for a binary tree node.
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
            
    
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        newNode = TreeNode(val)
        if root is None:
            return newNode
        #print(p, root.val)
        node = root
        while node:
            print(val, root.val)
            if val < node.val:
                if not node.left:
                    node.left = newNode
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = newNode
                    return root
                node = node.right
        return newNode
    
    
        
treelist = [7,3,6,2,4,1]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
val = 5
baby = (Solution().insertIntoBST(treeNode,val))
Solution().prettyPrintTree(baby,"",True)
        