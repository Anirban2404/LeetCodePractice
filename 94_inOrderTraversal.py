#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:45:31 2019

@author: anirban-mac
"""

"""
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
            

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        
        stack, inOrder = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inOrder.append(root.val)
            root = root.right
        

        return inOrder
        
        
    def inorderTraversalRecursive(self, root):
        if root is None:
            return None
        
        inOrder = []
        def recurse(root):
            if root:
                recurse(root.left)
                inOrder.append(root.val)
                recurse(root.right)
        recurse(root)
        return inOrder
    
    def MorrisTraversal(self, root):
        inOrder = []
        node = root
        while node:
            if node.left is None:
                inOrder.append(node.val)
                node = node.right
            else:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                
                if pre.right is None:
                    pre.right = node
                    node = node.left
                else:
                    pre.right = None
                    inOrder.append(node.val)
                    node = node.right
        return inOrder
        
treelist = [1,'null',2,3]
treeNode = Solution().stringToTreeNode(treelist)
Solution().prettyPrintTree(treeNode,"",True)
print(Solution().inorderTraversal(treeNode))
print(Solution().inorderTraversalRecursive(treeNode))
print(Solution().MorrisTraversal(treeNode))