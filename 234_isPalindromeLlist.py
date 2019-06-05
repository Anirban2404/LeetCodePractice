#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:40:49 2019

@author: anirban-mac
"""

"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

            
            
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # rev records the first half, need to set the same structure as fast, 
        # slow, hence later we have rev.next
        rev = None
        fast = slow =head
       
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
         
        return not rev
        
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
    
llist = [1,1,2,1]
node = Solution().stringToListNode(llist)
print(Solution().isPalindrome(node))