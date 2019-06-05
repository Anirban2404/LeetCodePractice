#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:55:49 2019

@author: anirban-mac
"""

"""
708. Insert into a Cyclic Sorted List

Given a node from a cyclic linked list which is sorted in ascending order, 
write a function to insert a value into the list such that it remains a cyclic 
sorted list. The given node can be a reference to any single node in the list, 
and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to 
insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single 
cyclic list and return the reference to that single node. Otherwise, you should 
return the original given node.

The following example may help you understand the problem better:

 



In the figure above, there is a cyclic sorted list of three elements. You are 
given a reference to the node with value 3, and we need to insert 2 into the list.

 



The new node should insert between node 1 and node 3. After the insertion, the 
list should look like this, and we should still return node 3.
"""

# Definition for a Node.
class Node:
    def __init__(self, val):#, next):
        self.val = val
        self.next = None#next

class Solution:

    def inputListNode(self,numbers): 
        # Now convert that list into linked list
        dummyRoot = Node(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = Node(number)
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
    
    
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        
        new_node = Node(insertVal, head)
        
        if not head:  
            return new_node
         
        node = head
        while True:
            if node.next.val < node.val and \
                (insertVal <= node.next.val or insertVal >= node.val):
                break
            elif node.val <= insertVal <= node.next.val:
                break
            elif node.next == head:
                break
            node = node.next
        
        new_node.next = node.next
        node.next = new_node
        return head
                
                
                
        
        
    
llist = [1,2,3,4,5]
insertVal = 1
node = Solution().inputListNode(llist)
print(Solution().printLinkedList(node))
inserted = Solution().insert(node, insertVal)
print(Solution().printLinkedList(inserted))