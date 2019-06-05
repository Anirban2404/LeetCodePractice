#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:00:25 2019

@author: anirban-mac
"""

"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value 
already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if 
this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the 
mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.size = 99999
        self.buckets = [[] for _ in range (self.size)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        bucketarr = self.buckets[bucket]
        if idx < 0:
            bucketarr.append((key, value))
        else:
            bucketarr[idx] = (key, value)
       
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return -1
        bucketarr = self.buckets[bucket]
        key, value = bucketarr[idx]
        return value


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucketarr = self.buckets[bucket]
        del bucketarr[idx]

        
    def _hash(self, key):
        return key % self.size
    
    
    def _index(self, key):
        #hash = self._hash(key)
        #bucket = self.buckets[hash]
        bucket = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket]):
        #for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1
        


# Your MyHashMap object will be instantiated and called as such:
hashMap = MyHashMap()
#obj.put(key,value)
hashMap.put(1, 1); 
hashMap.put(2, 5); 
hashMap.put(9, 3); 
hashMap.put(6, 7); 
print(hashMap.get(65));  
# param_2 = obj.get(key)
# obj.remove(key)
        