#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:51:47 2019

@author: anirban-mac
"""
"""
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        

        cur = head
        prev = None
        
        while m > 1:
            prev, cur = cur, cur.next
            m = m - 1
            n = n - 1
        
        lptr, rptr = prev, cur
        
        while n:
            cur.next, cur, prev = prev, cur.next, cur
            n -= 1
        
        if lptr:
            lptr.next = prev
        else:
            head = prev
        
        rptr.next = cur
        return head
            

linkedList = myLinkedList()
numbers = [1,2,3,4,5]
head = linkedList.inputListNode(numbers)
linkedList.printLinkedList(head)
m = 2
n = 4
reversedLL = Solution().reverseBetween(head, m, n)
linkedList.printLinkedList(reversedLL)