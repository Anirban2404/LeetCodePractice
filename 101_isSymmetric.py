#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:08:21 2019

@author: anirban-mac
"""

"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric 
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

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
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        return self.isMirror(root, root)
        """
        if root is None:
            return True
    
        stack, left, right = [], root.left, root.right
        
        while stack or left and right:
            if not (left or right):
                #inPair
                right = stack.pop().left
                left = stack.pop().right
            elif not left or not right or left.val != right.val:
                return False
            else:
                #outPair
                stack.append(left)
                stack.append(right)
                left, right = left.left, right.right

        return not (stack or left or right)
      
        """
    def isMirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False
        """
        
    """
    def isSymmetric(self, root):
        if root is None:
            return True
        queue = deque([root])
        queue.append(root)
        while queue:
            left = queue.pop()
            right = queue.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
    """
    
treelist = [1,2,2,3,4,4,3]
treeNode = Solution().stringToTreeNode(treelist)
print(Solution().isSymmetric(treeNode))
