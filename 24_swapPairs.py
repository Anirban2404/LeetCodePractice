#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:00:12 2019

@author: anirban-mac
"""

"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be 
changed.


Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def inputListNode(self,numbers): 
        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next
        
        ptr = dummyRoot.next
        return ptr
        
    def printLinkedList(self,node):
        while node and node.next:
            print(str(node.val) + "->", end='')
            node = node.next
        if node:
            print(node.val)
        else:
            print("Empty LinkedList")
            
     
    def swapPairs(self, head):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """    
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        
        prev = jump = ListNode(0)
        prev.next = lptr = rptr = head
        
        k = 2
        while True:
            count = 0
            while rptr and count < k:   
                rptr = rptr.next
                count += 1
            if count == k:  
                pre, cur = rptr, lptr
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  
                jump.next, jump, lptr = pre, lptr, rptr
            else:
                return prev.next
            


treeList = [1,2,3,4,5,6,7,8]
treeLL = Solution().inputListNode(treeList)
Solution().printLinkedList(treeLL)

swapLL= Solution().swapPairs(treeLL)
Solution().printLinkedList(swapLL)

