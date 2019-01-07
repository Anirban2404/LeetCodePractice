#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:17:44 2019

@author: anirban-mac
"""
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class myLinkedList:
    
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

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

linkedList = myLinkedList()
numbers = [1,2,3,4,5]
head = linkedList.inputListNode(numbers)
linkedList.printLinkedList(head)
reversedLL = Solution().reverseList(head)
linkedList.printLinkedList(reversedLL)