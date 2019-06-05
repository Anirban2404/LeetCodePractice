#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:23:41 2019

@author: anirban-mac
"""

"""
Given a linked list, rotate the list to the right by k places, where k is 
non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """  
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        old_tail = head
        size = 1
        
        while old_tail and old_tail.next:
            old_tail = old_tail.next
            size += 1  
        
        old_tail.next = head
        new_tail = head
        
        k = size - k % size - 1
        for i in range(k):
           new_tail = new_tail.next
           
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
            
    
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
    
llist = [0,1,2]
k = 4
node = Solution().stringToListNode(llist)
print(Solution().prettyPrintLinkedList(node))
rotateRightList = Solution().rotateRight(node, k)
print(Solution().prettyPrintLinkedList(rotateRightList))