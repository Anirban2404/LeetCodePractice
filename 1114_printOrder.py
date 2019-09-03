#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:03:03 2019

@author: anirban-mac
"""

"""
1114. Print in Order
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. 
Thread A will call first(), thread B will call second(), and thread C will
 call third(). Design a mechanism and modify the program to ensure that second()
 is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input 
[1,2,3] means thread A calls first(), thread B calls second(), and thread C 
calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls 
third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""

import threading


class Foo(object):
    def __init__(self):
        pass


    def first(self):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        print("First")


    def second(self):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        print("Second")
            
            
    def third(self):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        print("Third")
        

    
    def printOrder(self):
        threads = []
        for i in range(10):
            t_first = threading.Thread(target=self.first)
            t_second = threading.Thread(target=self.second)
            t_third = threading.Thread(target=self.third)
            
            threads.append(t_first)
            threads.append(t_second)
            threads.append(t_third)
            
            t_first.start()
            t_second.start()
            t_third.start()
            
thread = Foo()
print(thread.printOrder())