#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:29:30 2019

@author: anirban-mac
"""

"""
545. Boundary of Binary Tree
Given a binary tree, return the values of its boundary in anti-clockwise 
direction starting from root. Boundary includes left boundary, leaves, and 
right boundary in order without duplicate nodes.  (The values of the nodes may 
still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right 
boundary is defined as the path from root to the right-most node. If the root 
doesn't have left subtree or right subtree, then the root itself is left 
boundary or right boundary. Note this definition only applies to the input 
binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always 
firstly travel to the left subtree if exists. If not, travel to the right subtree. 
Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you 
should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
"""

# Definition for a binary tree node.
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
            
    
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Print root
        #print all left boundary node except leaf
        #print all leaf nodes
        #print all right boundary nodes(in reverse node)
        if root is None:
            return None
        
        antiClockOrder = []
        
         #print all left boundary node except leaf
        def printLefties(root):
            if root:
                if root.left:
                    antiClockOrder.append(root.val)
                    printLefties(root.left)
                elif root.right:
                    antiClockOrder.append(root.val)
                    printLefties(root.right)
        
        #print all leaf nodes     
        def printLeaves(root):
            if root:
                printLeaves(root.left)
                if root.left is None and root.right is None:
                    antiClockOrder.append(root.val)
                printLeaves(root.right)
           
        #print all right boundary nodes(in reverse node)
        def printRighties(root):
             if root:
                if root.right:
                    printRighties(root.right)
                    antiClockOrder.append(root.val)
                elif root.left:
                    printRighties(root.left)
                    antiClockOrder.append(root.val)
        
        if root:
            antiClockOrder.append(root.val)
            printLefties(root.left)
            printLeaves(root.left)
            printLeaves(root.right)
            printRighties(root.right)
        return antiClockOrder
    
treelist = [1,2,3,'null',4,5,'null',6,7,8,9,'null',10]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
print(Solution().boundaryOfBinaryTree(treeNode))