#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 10:50:32 2019

@author: anirban-mac
"""
"""
Design your implementation of the linked list. You can choose to use the singly
 linked list or the doubly linked list. A node in a singly linked list should 
 have two attributes: val and next. 
 -- val is the value of the current node, and 
 -- next is a pointer/reference to the next node. 
 
 
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Input:
    
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]

Output:
[null,null,null,null,2,null,3]   
"""

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index 
        is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size -1 or index < 0:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next        
        return cur.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the 
        linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(0, val)
    
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended
        to the end of linked list. If index is greater than the length, the 
        node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        
        if index > self.size:
            return
        
        if index < 0:
            index = 0
        
        newnode = ListNode(val)
        
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            self.size += 1
            return
        
        cur = self.head
        for i in range(1, index):
            cur = cur.next
        newnode.next = cur.next
        cur.next = newnode
        self.size += 1
    

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index > self.size -1 or index < 0:
            return
        
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        else:#CurrNode will be deleted
            cur = self.head
            for i in range(1, index):
                cur = cur.next
        
            cur.next = cur.next.next
            self.size -= 1
            

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val, "-->", end=" ", flush=True)
            printval = printval.next
        print (None)
        print ("Size:", self.size)


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()

linkedList.addAtHead(1)
#linkedList.addAtHead(5)
#linkedList.addAtHead(2)
#linkedList.listprint()
#linkedList.addAtTail(21)
#linkedList.listprint() 

index = -1
linkedList.addAtIndex(index,0)
linkedList.listprint()    

param_1 = linkedList.get(index)
print("Value at index", index , ":", param_1)
linkedList.listprint()  
index = 1
linkedList.deleteAtIndex(index)
linkedList.listprint()    