#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:14:58 2019

@author: anirban-mac
"""
"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return 
its modified list.

k is a positive integer and is less than or equal to the length of the linked 
list. If the number of nodes is not a multiple of k then left-out nodes in the 
end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        dummy = jump = ListNode(0)
        dummy.next = lptr = rptr = head
        
        while head.next:
            count = 0
            while rptr and count < k:   
                rptr = rptr.next
                count += 1
            if count == k:  
                prev, cur = rptr, lptr
                for _ in range(k):
                    cur.next, cur, prev = prev, cur.next, cur  
                jump.next, jump, lptr = prev, lptr, rptr
            else:
                return dummy.next

linkedList = myLinkedList()
numbers = [1,2,3,4,5]
head = linkedList.inputListNode(numbers)
linkedList.printLinkedList(head)
k = 2
reversedLL = Solution().reverseKGroup(head, k)
linkedList.printLinkedList(reversedLL)