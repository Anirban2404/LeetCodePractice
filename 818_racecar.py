#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:43:48 2019

@author: anirban-mac
"""

"""
818. Race Car
Your car starts at position 0 and speed +1 on an infinite number line.  
(Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A 
(accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, 
speed *= 2.

When you get an instruction "R", your car does the following: if your speed is 
positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and 
your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of 
instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.

"""
from collections import deque
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        #BFS
        q = deque([(0, 1)])
        visited = set([(0,1)])
        steps = 0
        
        while q:
            for _ in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return steps
                if not (pos + speed, speed * 2) in visited:
                    q.append((pos + speed, speed * 2))
                    visited.add((pos + speed, speed * 2))
                if not (pos, -1 if speed > 0 else 1) in visited:
                    q.append((pos, -1 if speed > 0 else 1))
                    visited.add((pos, -1 if speed > 0 else 1))
                    print(q)
            steps += 1
        
        
target = 26
print(Solution().racecar(target))