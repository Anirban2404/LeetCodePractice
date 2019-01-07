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

class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        headNode = Node(dataval = None)
        self.headval = headNode
        self.size = 0
        

    def getNode(self, index):
        """
        Get the value of the index-th node in the linked list. If the index 
        is invalid, return -1.
        :type index: int
        :rtype: Node
        """
        
        getNode = self.headval
        for i in range(index):
            getNode = getNode.nextval
        #print(getNode.dataval)
        return getNode 
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index 
        is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size -1 or index < 0:
            return -1
        else:
            currNode = self.getNode(index)
            return currNode.dataval
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the 
        linked list.
        :type val: int
        :rtype: void
        """
        newHeadNode = Node(dataval = val)
        if self.size>0:
            newHeadNode.nextval = self.headval
        self.headval = newHeadNode
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        newTailNode = Node(dataval = val)
        if self.size == 0:
            self.headval = newTailNode
        else:  
            currNode = self.headval
            for i in range(self.size-1):
                currNode = currNode.nextval
            currNode.nextval = newTailNode
        self.size += 1
        

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
        
        if index == 0:
            print("At head")
            self.addAtHead(val)
        elif index == self.size:
            print("At tail")
            self.addAtTail(val)
        elif index >= self.size or index < 0:
            print("Out of Range")
        else:
            print("At", index)
            
            newNode = Node(dataval = val)
            currNode = self.getNode(index-1)
            newNode.nextval = currNode.nextval
            currNode.nextval = newNode
            
            self.size += 1
    

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index > self.size -1 or index < 0:
            print("Out of Range")
        elif index == 0:
            self.headval = self.getNode(index+1)
            self.size -= 1
        else:#CurrNode will be deleted
            print("At", index)
            delNode = self.getNode(index - 1)
            currNode = self.getNode(index)
            delNode.nextval = currNode.nextval
            self.size -= 1
            

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval, "-->", end=" ", flush=True)
            printval = printval.nextval
        print (None)
        print ("Size:", self.size)


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()

linkedList.addAtHead(1)
linkedList.addAtHead(5)
linkedList.addAtHead(2)
linkedList.listprint()
linkedList.addAtTail(21)
linkedList.listprint() 

index = 4
linkedList.addAtIndex(index,24)
linkedList.listprint()    

param_1 = linkedList.get(index)
print("Value at index", index , ":", param_1)
linkedList.listprint()  
index = 1
linkedList.deleteAtIndex(index)
linkedList.listprint()    