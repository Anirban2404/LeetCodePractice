#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:06:27 2019

@author: anirban-mac
"""
"""
622. Design Circular Queue
Design your implementation of the circular queue. The circular queue is a 
linear data structure in which the operations are performed based on FIFO 
(First In First Out) principle and the last position is connected back to the 
first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces
in front of the queue. In a normal queue, once the queue becomes full, we 
cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the 
operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the 
operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

"""

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.front = 0
        self.rear = k - 1
        self.capacity = k
        self.Q = [None] * k
        self.size = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = value
        self.size += 1
        print(self.Q)
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.Q[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(self.Q)
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.Q[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.Q[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1));  # return true
print(circularQueue.enQueue(2));  # return true
print(circularQueue.enQueue(3));  # return true
print(circularQueue.enQueue(4));  # return false, the queue is full
print(circularQueue.Rear());  # return 3
print(circularQueue.isFull());  # return true
print(circularQueue.deQueue());  # return true
print(circularQueue.enQueue(4));  # return true
print(circularQueue.Rear());  # return 4
print(circularQueue.Front())
