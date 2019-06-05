#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:32:57 2019

@author: anirban-mac
"""

"""
Write a program to find the node at which the intersection of two singly linked 
lists begins.

For example, the following two linked lists:
A: a1 -> a2 -> c1 -> c2 -> c3
B: b1 -> b2 -> b3 -> c1 -> c2 -> c3
begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], 
skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must 
not be 0 if the two lists intersect). From the head of A, it reads as 
[4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 
nodes before the intersected node in A; There are 3 nodes before the 
intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], 
skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not
 be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. 
From the head of B, it reads as [3,2,4]. There are 3 nodes before the 
intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B,
it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 
0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        p = headA
        q = headB
       
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
        
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
    
list1 = [4,1,8,4,5]
list2 = [5,0,1,8,4,5]
node1 = Solution().stringToListNode(list1)
#Solution().prettyPrintLinkedList(node1)
node2 = Solution().stringToListNode(list2)
#Solution().prettyPrintLinkedList(node2)
print(Solution().getIntersectionNode(node1,node2))

