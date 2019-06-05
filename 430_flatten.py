#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:47:16 2019

@author: anirban-mac
"""

"""
430 . Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous 
pointers, it could have a child pointer, which may or may not point to a 
separate doubly linked list. These child lists may have one or more children 
of their own, and so on, to produce a multilevel data structure, as shown in 
the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked 
list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return
        
        curr, stack = head, []
        
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future 
                    # reattachment
                    stack.append(curr.next)
                    
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            if not curr.next and len(stack):
                # If the current node is a child without a next pointer
                temp = stack.pop()
                # Current <-> Temp
                temp.prev, curr.next = curr, temp
            curr = curr.next
        return head
            