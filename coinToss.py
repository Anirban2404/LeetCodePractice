#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:59:09 2019

@author: anirban-mac
"""

import random

class Toss:
    def toss(self):
        low = 1
        high = 1000000
        result = random.randint(low,high)
        #print(result)
        if 1- result & 1:
            return "head"
        else:
            return "tail"
            
    def test(self):
        countHead, countTail = 0, 0
        for _ in range(pow(10,7)-1):
            if self.toss() == "head":
                countHead += 1
            else:
                countTail += 1
        totalToss = countHead + countTail
        print("Head:", countHead, ',', "Tail:", countTail)
        print("Probability of Head:", countHead/totalToss)
        print("Probability of Tail:", countTail/totalToss)
                
    def selectFate(self, select):
        result = self.toss()
        print(result)
        if select == result:
            return "Won"
        else:
            return "Lost"
        
select = input("What is your choice? head or tail\n")        
print(Toss().selectFate(select))
#print(Toss().test())
