#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:14:08 2019

@author: anirban-mac
"""

"""
654. Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this 
array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray 
divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray 
divided by the maximum number.
Construct the maximum tree by the given array and output the root node of 
this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        maxval = max(nums)
        max_i = nums.index(maxval)
        root = TreeNode(int(maxval))
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
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

treelist = [3,2,1,6,0,5]

treeNode = Solution().constructMaximumBinaryTree(treelist)
Solution().prettyPrintTree(treeNode,"",True)