#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:30:27 2019

@author: anirban-mac
"""
"""
225. Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
"""
from queue import Queue 
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        self.size = self.q.qsize()
        while self.size > 1:
            self.q.put(self.q.get())
            self.size -= 1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q.empty(): 
            return -1
        return self.q.queue[0] 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q.qsize() == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
stack = MyStack()
stack.push(1);
#stack.push(2); 
param_2 = stack.pop()
print(param_2)
param_3 = stack.top()
print(param_3)
param_4 = stack.empty()
print(param_4)