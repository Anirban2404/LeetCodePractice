#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:29:06 2019

@author: anirban-mac
"""
"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its 
head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        
        # two pass
        """
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        # print(size)
        deleteAtIndex = size - n 
        print (deleteAtIndex)
        
        
        if deleteAtIndex <= 0:
            head = head.next
            return head
        
        cur = head
        for i in range(1, deleteAtIndex):
            cur = cur.next
        cur.next = cur.next.next
    
        return head
        """ 
        #one pass
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy 
        
        if first.next is None:
            return
        
        for i in range(1, n+1):
            second = second.next 
            #print(second.val)
            if second.next is None:
                head = head.next
                return head
            
        while second.next:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        
        return dummy.next
        
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
    
llist = [1,2]
n = 2
node = Solution().stringToListNode(llist)
print(Solution().prettyPrintLinkedList(node))
removed = Solution().removeNthFromEnd(node, n)
print(Solution().prettyPrintLinkedList(removed))