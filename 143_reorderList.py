#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:52:50 2019

@author: anirban-mac
"""

"""
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be 
changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        # detach left half of the list from the right half
        prev = slow.next = None
        
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
         
        ptr1, ptr2 = head, prev
        while ptr2:
            tmp1, tmp2 = ptr1.next, ptr2.next
            ptr1.next, ptr2.next = ptr2, tmp1
            ptr1, ptr2 = tmp1, tmp2
            
        return head
            
        

linkedList = myLinkedList()
numbers = [1,2,3,4,5,6,7]
head = linkedList.inputListNode(numbers)
linkedList.printLinkedList(head)
reorderedLL = Solution().reorderList(head)
linkedList.printLinkedList(reorderedLL)