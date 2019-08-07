#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:05:02 2019

@author: anirban-mac
"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return 
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        carry = 0
        sum = 0
        sumNode = curr = ListNode(0)
        while l1 is not None or l2 is not None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = carry + x + y
            carry = sum // 10
            sumdigit = sum % 10
            #print(sumdigit)
            curr.next = ListNode(sumdigit)
            curr = curr.next
            if (l1 != None):
                l1 = l1.next;
            if (l2 != None):
                l2 = l2.next;
        if (carry>0):
            curr.next = ListNode(carry)
        #sumNode = sumNode.next
        #print(self.prettyPrintLinkedList(sumNode))
        return sumNode.next
        
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

list1 = [5,4,3]
list2 = [9,6,4,5,0,1]
node1 = Solution().stringToListNode(list1)
#Solution().prettyPrintLinkedList(node1)
node2 = Solution().stringToListNode(list2)
#Solution().prettyPrintLinkedList(node2)
sumNode = Solution().addTwoNumbers(node1,node2)
Solution().prettyPrintLinkedList(sumNode)
