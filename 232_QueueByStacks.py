#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:34:00 2019

@author: anirban-mac
"""

"""
232. Implement Queue using Stacks
mplement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to 
top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may 
simulate a stack by using a list or deque (double-ended queue), as long as 
you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek 
operations will be called on an empty queue).
"""
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.instack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.instack == [] and self.outstack == []
        


# Your MyQueue object will be instantiated and called as such:
q = MyQueue()
q.push(2)
q.push(2)
param_2 = q.pop()
print(param_2)
param_3 = q.peek()
print(param_3)
param_4 = q.empty()
print(param_4)