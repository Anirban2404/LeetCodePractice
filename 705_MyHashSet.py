#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:36:06 2019

@author: anirban-mac
"""

"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in 
the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 99999
        self.buckets = [[] for _ in range (self.size)]
        
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        _, idx = self._index(key)
        return idx >= 0
    
    def _hash(self, key):
        return key % self.size
    
    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1
        


# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(1)
hashSet.remove(1)
# param_3 = obj.contains(key)