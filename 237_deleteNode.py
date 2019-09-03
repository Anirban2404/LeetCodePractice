#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:23:18 2019

@author: anirban-mac
"""

"""
237. Delete Node in a Linked List
Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

4 -> 5 -> 1 -> 9

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should 
become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should 
become 4 -> 5 -> 9 after calling your function.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def deleteNode(self, node, value):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """        
        head = node
        cur = head
        while cur:
            cur = cur.next
            if cur.val == value:
                cur.val = cur.next.val
                cur.next = cur.next.next
                break
        return head
            
        
    def stringToListNode(self, input):
        # Generate list from the input
        numbers = (input)
    
        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next
    
        ptr = dummyRoot.next
        return ptr
    
    def prettyPrintLinkedList(self, node):
        while node and node.next:
            print(str(node.val) + "->", end='')
            node = node.next
        
        if node:
            print(node.val)
        else:
            print("Empty LinkedList")
    
llist = [1,2,3,4,5]
node = Solution().stringToListNode(llist)
print(Solution().prettyPrintLinkedList(node))
value = 4
deletedllist = Solution().deleteNode(node,value)
print(Solution().prettyPrintLinkedList(deletedllist))