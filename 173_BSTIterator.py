#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:18:37 2019

@author: anirban-mac
"""

"""
285. Inorder Successor in BST
Implement an iterator over a binary search tree (BST). Your iterator will be 
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, 
where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at 
least a next smallest number in the BST when next() is called.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """       
        self.stack = []
        self.pushAll(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
    
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.stack)>0:
            return True
        return False

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
            

