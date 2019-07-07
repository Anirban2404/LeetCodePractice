#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:13:55 2019

@author: anirban-mac
"""
"""
// Problem - For given two integer arrays, 
//find numbers in the first array which are NOT present
// in the second array.

// Expectations:        
//                1.    Give sample so that we are all clear so far as understanding goes.
//                2.    3 parts: main, IO method and algorithm implementation. Focus on the last part.

//A = {21,32,23,34,55,0} null
//B = {21,23,32,41}  
//result = {34,55,0}
//---------------------

"""
import collections
#print "Hello"
def find(A, B):

  secondDict = collections.Counter(B)

  #print(secondDict)

  distarr = []
  for num in A:
    if num not in secondDict:
      distarr.append(num)
    else:
      secondDict[num] -= 1
      if secondDict[num] == 0:
        del secondDict[num]
  return distarr



A = [21,21,21,21, 32,23,34,55,0]
B = [21,21,23,32,41]
print(find(A,B))