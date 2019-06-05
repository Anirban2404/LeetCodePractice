#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:48:54 2019

@author: anirban-mac
"""
"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and 
describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from queue import PriorityQueue
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
            
     
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """    
        nodes = []
        mergedNode = curr = ListNode(-1)
        for treeList in lists:
            while treeList:
                nodes.append(treeList.val)
                treeList = treeList.next
                
        for x in sorted(nodes):
            curr.next = ListNode(x)
            curr = curr.next
        return mergedNode.next

    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        mergedNode = curr = ListNode(-1)
        q = PriorityQueue()
        for i,treeList in enumerate(lists):
            if treeList: 
                q.put((treeList.val, i, treeList))
                
        while q.qsize()>0:
            _, i, curr.next = q.get()
            curr = curr.next
            if curr.next: 
                q.put((curr.next.val, i, curr.next))
        return mergedNode.next

treeLists = []
lists = [[1,4,5],[1,3,4],[2,6]]
for l in lists:
    treeLists.append(Solution().inputListNode(l))
for treeList in treeLists:
    Solution().printLinkedList(treeList)


mergedK= Solution().mergeKLists(treeLists)
Solution().printLinkedList(mergedK)

mergedK= Solution().mergeKLists2(treeLists)
Solution().printLinkedList(mergedK)