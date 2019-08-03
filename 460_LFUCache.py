#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:06:20 2019

@author: anirban-mac
"""

"""
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists 
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reaches its capacity, it should invalidate the least frequently 
used item before inserting a new item. For the purpose of this problem, when 
there is a tie (i.e., two or more keys that have the same frequency), the least 
recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cacheFreq = defaultdict(OrderedDict)
        self.cacheKey = {}
        self.leastFreq = 1
    
    def _evict(self):
        key, _ = self.cacheFreq[self.leastFreq].popitem(last=False)
        del self.cacheKey[key]
    
    def _update(self, key, value):
        freq = self.cacheKey[key]['freq']
        val = self.cacheKey[key]['value']
        del self.cacheFreq[freq][key]
        if not self.cacheFreq[self.leastFreq]:
            self.leastFreq += 1
        self.cacheKey[key] = {'freq': freq + 1, 'value': value or val}
        self.cacheFreq[freq + 1][key] = value or val
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cacheKey:
            return -1
        self._update(key, None)
        return self.cacheKey[key]['value']
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cacheKey:
            self._update(key, value)
            return
        self.cacheKey[key] = {'freq': 1, 'value': value}
        self.cacheFreq[1][key] = value
        if len(self.cacheKey) > self.capacity:
            self._evict()
        self.leastFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)